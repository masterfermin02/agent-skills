---
name: csharp-unit-testing
description: "Write, review, and improve unit tests specifically in C# using xUnit, Moq, and FluentAssertions. Use when working with C# or .NET test projects, writing xUnit tests, using Moq for mocking, FluentAssertions for assertions, or applying C#-specific patterns like Theory/InlineData parameterized tests, IClassFixture, or xUnit test organization. Extends the general unit-testing skill with C#-specific examples and stack guidance. Triggers on write a C# test, xUnit test, Moq mock, FluentAssertions, C# unit test, .NET test project, Theory InlineData, add tests to my C# class."
---

# C# Unit Testing Skill

## Installation

```bash
# via skills.sh
npx skillsadd masterfermin02/agent-skills --skill csharp-unit-testing

# via ClaWHub
npx clawhub@latest install masterfermin02/agent-skills/csharp-unit-testing

# manual
git clone https://github.com/masterfermin02/agent-skills.git
cp -r agent-skills/csharp-unit-testing ~/.openclaw/skills/
```

C#-specific unit testing guidance using **xUnit + Moq + FluentAssertions**.

> This skill extends the general `unit-testing` skill. All framework-agnostic principles (AAA, Object Mother, Builder, test doubles, anti-patterns) apply here — refer to that skill's references for full detail. This skill adds C#-specific patterns and stack guidance.

## Stack

| Concern | Library |
|---------|---------|
| Test framework | [xUnit](https://xunit.net/) |
| Mocking | [Moq](https://github.com/devlooped/moq) |
| Assertions | [FluentAssertions](https://fluentassertions.com/) |

## Project Setup

```xml
<!-- .csproj -->
<PackageReference Include="xunit" Version="2.*" />
<PackageReference Include="xunit.runner.visualstudio" Version="2.*" />
<PackageReference Include="Moq" Version="4.*" />
<PackageReference Include="FluentAssertions" Version="6.*" />
<PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.*" />
```

## Test Structure

```csharp
public class SubscriptionTests
{
    [Fact]
    public void Deactivating_AnActiveSubscription_Succeeds()
    {
        // Arrange
        var sut = SubscriptionMother.Active();

        // Act
        sut.Deactivate();

        // Assert
        sut.Status.Should().Be(SubscriptionStatus.Inactive);
    }

    [Theory]
    [InlineData("pass", false)]
    [InlineData("ValidPass1!", true)]
    public void Validating_Password_ReturnsExpectedResult(string password, bool expected)
    {
        var sut = new PasswordValidator();
        sut.Validate(password).IsValid.Should().Be(expected);
    }
}
```

## C#-Specific Patterns

### Exceptions
```csharp
// FluentAssertions exception assertion
var act = () => sut.Deactivate();
act.Should().Throw<InvalidOperationException>()
   .WithMessage("*already inactive*");
```

### Async Tests
```csharp
[Fact]
public async Task PlacingOrder_Async_PersistsSuccessfully()
{
    var repository = new InMemoryOrderRepository();
    var sut = new OrderService(repository);

    await sut.PlaceAsync(OrderMother.Valid());

    repository.Count.Should().Be(1);
}
```

### Moq — when you must use it
```csharp
// Stub a return value
var stub = new Mock<IExternalPricingService>();
stub.Setup(x => x.GetPrice(It.IsAny<string>())).Returns(99.99m);

// Verify interaction (last resort — prefer Spy)
mock.Verify(m => m.Send(It.Is<Email>(e => e.To == "user@test.com")), Times.Once);
```

### Shared Setup (use carefully — avoid shared mutable state)
```csharp
// IClassFixture for expensive read-only setup only
public class OrderServiceTests : IClassFixture<DatabaseFixture>
{
    private readonly DatabaseFixture _fixture;
    public OrderServiceTests(DatabaseFixture fixture) { _fixture = fixture; }
}
```

## Reference

This skill references the general unit-testing skill at:
`../unit-testing/`

Full pattern examples (Object Mother, Builder, Assert Object, Parameterized) and anti-patterns are documented there in:
- `references/patterns.md`
- `references/anti-patterns.md`
- `references/test-doubles.md`

Source material: [masterfermin02/unit-testing-tips-csharp](https://github.com/masterfermin02/unit-testing-tips-csharp)
