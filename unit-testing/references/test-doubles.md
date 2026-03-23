# Test Doubles Reference

## Fake

A working but simplified implementation. Replaces real infrastructure.

**C#:**
```csharp
public class InMemoryOrderRepository : IOrderRepository
{
    private readonly Dictionary<Guid, Order> _store = new();
    public void Save(Order order) => _store[order.Id] = order;
    public Order Get(Guid id) => _store[id];
    public int Count => _store.Count;
}
```

**PHP:**
```php
class InMemoryOrderRepository implements OrderRepositoryInterface
{
    private array $store = [];
    public function save(Order $order): void { $this->store[$order->id()] = $order; }
    public function get(string $id): Order { return $this->store[$id]; }
    public function count(): int { return count($this->store); }
}
```

**TypeScript/Jest:**
```typescript
class InMemoryOrderRepository implements OrderRepository {
    private store = new Map<string, Order>();
    save(order: Order): void { this.store.set(order.id, order); }
    get(id: string): Order { return this.store.get(id)!; }
    get count(): number { return this.store.size; }
}
```

---

## Stub

Returns predefined values to control SUT behavior.

**C# (custom):**
```csharp
public class AlwaysUniqueEmailStub : IUniqueEmailSpecification
{
    public bool IsUnique(string email) => true;
}
```

**C# (Moq):**
```csharp
var stub = new Mock<IUniqueEmailSpecification>();
stub.Setup(x => x.IsUnique(It.IsAny<string>())).Returns(true);
```

**PHP (Prophecy/PHPUnit):**
```php
$stub = $this->createStub(UniqueEmailSpecificationInterface::class);
$stub->method('isUnique')->willReturn(true);
```

**TypeScript (Jest):**
```typescript
const stub = { isUnique: jest.fn().mockReturnValue(true) };
```

**Java (Mockito):**
```java
UniqueEmailSpec stub = mock(UniqueEmailSpec.class);
when(stub.isUnique(anyString())).thenReturn(true);
```

---

## Spy

Records interactions for assertion after the Act phase.

**C#:**
```csharp
public class SpyMailer : IMailer
{
    public List<Message> SentMessages { get; } = new();
    public void Send(Message message) => SentMessages.Add(message);
    public int SentCount => SentMessages.Count;
    public bool WasSentTo(string email) => SentMessages.Any(m => m.To == email);
}
```

**PHP:**
```php
class SpyMailer implements MailerInterface
{
    public array $sentMessages = [];
    public function send(Message $message): void { $this->sentMessages[] = $message; }
    public function sentCount(): int { return count($this->sentMessages); }
}
```

**TypeScript:**
```typescript
class SpyMailer implements Mailer {
    sentMessages: Message[] = [];
    send(message: Message): void { this.sentMessages.push(message); }
    get sentCount(): number { return this.sentMessages.length; }
}
```

---

## Mock

Pre-configured to verify specific interactions. Use sparingly — prefer Spy.

**C# (Moq):**
```csharp
var mock = new Mock<IMailer>();
// ... act ...
mock.Verify(m => m.Send(It.Is<Message>(msg => msg.To == "user@example.com")), Times.Once);
```

**PHP (Prophecy):**
```php
$mock = $this->prophesize(MailerInterface::class);
$mock->send(Argument::that(fn($m) => $m->to === 'user@example.com'))->shouldBeCalledOnce();
$sut = new NotificationService($mock->reveal());
```

**Java (Mockito):**
```java
Mailer mock = mock(Mailer.class);
// ... act ...
verify(mock, times(1)).send(argThat(m -> m.getTo().equals("user@example.com")));
```

---

## Dummy

Satisfies a required parameter that is never used in the test.

**C#:**
```csharp
public class DummyMailer : IMailer
{
    public void Send(Message message) { /* intentionally empty */ }
}
```

**TypeScript:**
```typescript
const dummyMailer: Mailer = { send: () => {} };
```
