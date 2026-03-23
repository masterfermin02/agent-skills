# Unit Testing Anti-Patterns

## Table of Contents
1. [Overusing Mocks](#1-overusing-mocks)
2. [Testing Implementation Details](#2-testing-implementation-details)
3. [Poor Test Names](#3-poor-test-names)
4. [Multiple Acts in One Test](#4-multiple-acts-in-one-test)
5. [Shared Mutable State in Fixtures](#5-shared-mutable-state-in-fixtures)
6. [Getters Added Only for Tests](#6-getters-added-only-for-tests)
7. [Trivial Tests](#7-trivial-tests)
8. [Fragile Mock Verification](#8-fragile-mock-verification)

---

## 1. Overusing Mocks

**❌ Bad — every dependency mocked:**
```csharp
[Fact]
public void Sends_AllNotifications()
{
    var repo = new Mock<IMessageRepository>();
    repo.Setup(x => x.GetAll()).Returns(new[] { msg1, msg2 });
    var mailer = new Mock<IMailer>();
    var sut = new NotificationService(mailer.Object, repo.Object);
    sut.Send();
    mailer.Verify(x => x.Send(msg1), Times.Once);
    mailer.Verify(x => x.Send(msg2), Times.Once);
}
```

**✅ Good — fake + spy:**
```csharp
[Fact]
public void Sends_AllNotifications()
{
    var repository = new InMemoryMessageRepository();
    repository.Save(msg1); repository.Save(msg2);
    var mailer = new SpyMailer();
    var sut = new NotificationService(mailer, repository);
    sut.Send();
    mailer.SentMessages.Should().BeEquivalentTo(new[] { msg1, msg2 });
}
```

---

## 2. Testing Implementation Details

**❌ Bad — inspecting internals via reflection:**
```csharp
[Fact]
public void Hashing_SetsInternalSalt()
{
    var sut = new PasswordHasher();
    sut.Hash("password123");
    var salt = typeof(PasswordHasher)
        .GetField("_salt", BindingFlags.NonPublic | BindingFlags.Instance)!
        .GetValue(sut);
    salt.Should().NotBeNull(); // internal detail!
}
```

**✅ Good — test observable behavior:**
```csharp
[Fact]
public void Hashing_SamePassword_Twice_ProducesDifferentHashes()
{
    var sut = new PasswordHasher();
    var hash1 = sut.Hash("password123");
    var hash2 = sut.Hash("password123");
    hash1.Should().NotBe(hash2);
}
```

---

## 3. Poor Test Names

**❌ Bad:**
```
Test()
TestDeactivateSubscription()
ItThrowsWhenPasswordTooShort()
DeactivateSubscription_ShouldSetStatusToInactive()
```

**✅ Good:**
```
Deactivating_AnActiveSubscription_Succeeds()
Creating_WithTooShortPassword_IsInvalid()
PlacingOrder_WithNoItems_Fails()
SigningIn_WithInvalidCredentials_IsNotPossible()
```

Rules: no Test/Should/Assert/Verify. Underscores. Readable by non-developers.

---

## 4. Multiple Acts in One Test

**❌ Bad:**
```csharp
[Fact]
public void Managing_SubscriptionLifecycle()
{
    var sub = new Subscription(SubscriptionStatus.Active);
    sub.Deactivate();
    sub.Status.Should().Be(SubscriptionStatus.Inactive); // act+assert 1
    sub.Reactivate();
    sub.Status.Should().Be(SubscriptionStatus.Active);   // act+assert 2
}
```

**✅ Good — one behavior per test:**
```csharp
[Fact]
public void Deactivating_AnActiveSubscription_SetsStatusToInactive() { ... }

[Fact]
public void Reactivating_AnInactiveSubscription_SetsStatusToActive() { ... }
```

---

## 5. Shared Mutable State in Fixtures

**❌ Bad — shared state causes test order dependency:**
```csharp
public class OrderTests
{
    private readonly InMemoryOrderRepository _repository = new(); // shared!

    [Fact]
    public void FirstTest() { _repository.Save(order1); /* ... */ }

    [Fact]
    public void SecondTest() { /* _repository may already have order1 */ }
}
```

**✅ Good — fresh state per test:**
```csharp
[Fact]
public void FirstTest()
{
    var repository = new InMemoryOrderRepository(); // fresh
    repository.Save(order1);
    // ...
}
```

---

## 6. Getters Added Only for Tests

**❌ Bad — exposing internal state only for tests:**
```csharp
public class Subscription
{
    private DateTime _renewalDate;
    public DateTime RenewalDate => _renewalDate; // only for tests!
    public void Renew() { _renewalDate = DateTime.UtcNow.AddMonths(1); }
}
```

**✅ Good — verify through domain behavior:**
```csharp
[Fact]
public void Renewing_ASubscription_AllowsAccessForAnotherMonth()
{
    var sut = new Subscription(SubscriptionStatus.Active, new FixedClock(jan1));
    sut.Renew();
    sut.IsActiveAt(jan31).Should().BeTrue();
    sut.IsActiveAt(feb2).Should().BeFalse();
}
```

---

## 7. Trivial Tests

**❌ Skip — no logic:**
```csharp
[Fact]
public void Customer_Name_IsSet()
{
    var customer = new Customer { Name = "Alice" };
    customer.Name.Should().Be("Alice"); // tests the language, not your code
}
```

**✅ Test — has real logic:**
```csharp
[Fact]
public void Discount_ForPremiumCustomer_IsTwentyPercent()
{
    var sut = new DiscountCalculator();
    var result = sut.Calculate(CustomerTier.Premium, 100m);
    result.Should().Be(20m);
}
```

---

## 8. Fragile Mock Verification

**❌ Bad — coupled to internal call sequence:**
```csharp
mockValidator.Verify(v => v.Validate(It.IsAny<Order>()), Times.Once);
mockPersister.Verify(p => p.Save(It.IsAny<Order>()), Times.Once);
// Breaks if you inline the validator — even if behavior is unchanged
```

**✅ Good — verify the outcome:**
```csharp
var repository = new InMemoryOrderRepository();
sut.Process(OrderMother.Valid());
repository.Count.Should().Be(1);
```
