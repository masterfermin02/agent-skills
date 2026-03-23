# Unit Testing Patterns Reference

## Table of Contents
1. [Object Mother](#object-mother)
2. [Builder Pattern](#builder-pattern)
3. [Assert Object / Custom Assertions](#assert-object)
4. [Parameterized Tests](#parameterized-tests)

---

## Object Mother

Static factory for pre-configured, semantically named test objects. Eliminates duplication in Arrange phases.

**C#:**
```csharp
public static class SubscriptionMother
{
    public static Subscription New() => new(SubscriptionStatus.New);
    public static Subscription Active() => new(SubscriptionStatus.Active);
    public static Subscription Inactive() => new(SubscriptionStatus.Inactive);
    public static Subscription ActiveWithPlan(SubscriptionPlan plan) =>
        new(SubscriptionStatus.Active, plan);
}

// Usage
var sut = SubscriptionMother.Active();
```

**PHP:**
```php
final class SubscriptionMother
{
    public static function active(): Subscription
    {
        return new Subscription(SubscriptionStatus::ACTIVE);
    }

    public static function inactive(): Subscription
    {
        return new Subscription(SubscriptionStatus::INACTIVE);
    }
}
```

**TypeScript:**
```typescript
export const SubscriptionMother = {
    active: (): Subscription => new Subscription(SubscriptionStatus.Active),
    inactive: (): Subscription => new Subscription(SubscriptionStatus.Inactive),
    activeWithPlan: (plan: Plan): Subscription =>
        new Subscription(SubscriptionStatus.Active, plan),
};
```

**Java:**
```java
public class SubscriptionMother {
    public static Subscription active() {
        return new Subscription(SubscriptionStatus.ACTIVE);
    }
    public static Subscription inactive() {
        return new Subscription(SubscriptionStatus.INACTIVE);
    }
}
```

---

## Builder Pattern

Fluent builder for complex objects with many optional fields. More flexible than Object Mother when many combinations exist.

**C#:**
```csharp
public class OrderBuilder
{
    private CustomerId _customerId = CustomerId.New();
    private List<OrderItem> _items = new() { new OrderItem("Product", 10m, 1) };
    private string _currency = "USD";

    public OrderBuilder WithCustomer(CustomerId id) { _customerId = id; return this; }
    public OrderBuilder WithItems(params OrderItem[] items) { _items = items.ToList(); return this; }
    public OrderBuilder WithCurrency(string currency) { _currency = currency; return this; }
    public OrderBuilder WithNoItems() { _items = new(); return this; }

    public Order Build() => new(_customerId, _items, _currency);
}

// Usage
var order = new OrderBuilder()
    .WithCustomer(customerId)
    .WithItems(new OrderItem("Widget", 25m, 3))
    .Build();
```

**TypeScript:**
```typescript
class OrderBuilder {
    private customerId = CustomerId.generate();
    private items: OrderItem[] = [{ name: 'Product', price: 10, qty: 1 }];
    private currency = 'USD';

    withCustomer(id: CustomerId): this { this.customerId = id; return this; }
    withItems(...items: OrderItem[]): this { this.items = items; return this; }
    withNoItems(): this { this.items = []; return this; }
    build(): Order { return new Order(this.customerId, this.items, this.currency); }
}
```

**PHP:**
```php
final class OrderBuilder
{
    private CustomerId $customerId;
    private array $items = [['name' => 'Product', 'price' => 10.0, 'qty' => 1]];
    private string $currency = 'USD';

    public function __construct() { $this->customerId = CustomerId::generate(); }

    public function withCustomer(CustomerId $id): self { $this->customerId = $id; return $this; }
    public function withNoItems(): self { $this->items = []; return $this; }
    public function build(): Order { return new Order($this->customerId, $this->items, $this->currency); }
}
```

---

## Assert Object

Encapsulate complex or repeated assertion logic into a reusable class. Improves readability and reduces duplication.

**C#:**
```csharp
public class OrderAssert
{
    private readonly Order _order;
    public OrderAssert(Order order) { _order = order; }

    public static OrderAssert For(Order order) => new(order);

    public OrderAssert HasStatus(OrderStatus expected)
    {
        _order.Status.Should().Be(expected);
        return this;
    }

    public OrderAssert HasItemCount(int expected)
    {
        _order.Items.Should().HaveCount(expected);
        return this;
    }

    public OrderAssert BelongsTo(CustomerId customerId)
    {
        _order.CustomerId.Should().Be(customerId);
        return this;
    }
}

// Usage
OrderAssert.For(order)
    .HasStatus(OrderStatus.Confirmed)
    .HasItemCount(2)
    .BelongsTo(customerId);
```

**TypeScript:**
```typescript
class OrderAssert {
    constructor(private readonly order: Order) {}

    static for(order: Order): OrderAssert { return new OrderAssert(order); }

    hasStatus(expected: OrderStatus): this {
        expect(this.order.status).toBe(expected);
        return this;
    }

    hasItemCount(expected: number): this {
        expect(this.order.items).toHaveLength(expected);
        return this;
    }
}
```

---

## Parameterized Tests

Test multiple input/output combinations without duplicating test code.

**C# (xUnit Theory):**
```csharp
[Theory]
[InlineData("password", false)]
[InlineData("pass", false)]
[InlineData("ValidPass1!", true)]
[InlineData("AnotherValid9#", true)]
public void Validating_Password_ReturnsExpectedResult(string password, bool expectedValid)
{
    var sut = new PasswordValidator();
    var result = sut.Validate(password);
    result.IsValid.Should().Be(expectedValid);
}
```

**PHP (PHPUnit DataProvider):**
```php
#[DataProvider('passwordProvider')]
public function test_validating_password(string $password, bool $expectedValid): void
{
    $sut = new PasswordValidator();
    $result = $sut->validate($password);
    $this->assertSame($expectedValid, $result->isValid());
}

public static function passwordProvider(): array
{
    return [
        ['password', false],
        ['pass', false],
        ['ValidPass1!', true],
    ];
}
```

**TypeScript (Jest each):**
```typescript
test.each([
    ['password', false],
    ['pass', false],
    ['ValidPass1!', true],
])('Validating "%s" returns %s', (password, expected) => {
    const sut = new PasswordValidator();
    expect(sut.validate(password).isValid).toBe(expected);
});
```

**Java (JUnit ParameterizedTest):**
```java
@ParameterizedTest
@CsvSource({"password,false", "pass,false", "ValidPass1!,true"})
void validating_password_returnsExpectedResult(String password, boolean expected) {
    var sut = new PasswordValidator();
    assertThat(sut.validate(password).isValid()).isEqualTo(expected);
}
```
