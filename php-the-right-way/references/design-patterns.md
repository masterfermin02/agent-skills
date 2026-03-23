# Design Patterns in PHP — The Right Way

Source: https://phptherightway.com/pages/Design-Patterns.html

## Factory

Centralizes object creation. Change the class in one place instead of everywhere.

```php
class Automobile
{
    public function __construct(
        private readonly string $make,
        private readonly string $model,
    ) {}

    public function getMakeAndModel(): string
    {
        return "{$this->make} {$this->model}";
    }
}

class AutomobileFactory
{
    public static function create(string $make, string $model): Automobile
    {
        return new Automobile($make, $model);
    }
}

$car = AutomobileFactory::create('Toyota', 'Corolla');
```

Use when: object creation is complex or you need to swap implementations.
Avoid when: creation is trivial — adds unnecessary indirection.

## Singleton

Ensures only one instance exists. Use sparingly — prefer dependency injection.

```php
class Config
{
    private static ?self $instance = null;

    private function __construct() {}
    private function __clone() {}

    public static function getInstance(): static
    {
        if (static::$instance === null) {
            static::$instance = new static();
        }
        return static::$instance;
    }
}
```

⚠️ Warning: Singletons introduce global state and hurt testability. Prefer DI containers.

## Strategy

Encapsulates interchangeable algorithms behind a common interface.

```php
interface OutputInterface
{
    public function render(array $data): string;
}

class JsonOutput implements OutputInterface
{
    public function render(array $data): string
    {
        return json_encode($data);
    }
}

class XmlOutput implements OutputInterface
{
    public function render(array $data): string
    {
        // build XML...
    }
}

class Exporter
{
    public function __construct(private OutputInterface $output) {}

    public function export(array $data): string
    {
        return $this->output->render($data);
    }
}

// Usage
$exporter = new Exporter(new JsonOutput());
echo $exporter->export(['key' => 'value']);
```

## Front Controller

Single entry point for all requests. Common in frameworks (index.php).

```php
// public/index.php
declare(strict_types=1);

require_once '../vendor/autoload.php';

$request = new Request($_SERVER, $_GET, $_POST);
$router  = new Router();
$router->dispatch($request);
```

## MVC (Model-View-Controller)

Most common PHP architectural pattern.

- **Model**: data access, business rules (no HTTP awareness)
- **Controller**: handles request, calls model, passes data to view
- **View**: presentation only (no business logic, no DB queries)

```
Request → Controller → Model → Controller → View → Response
```

Rules:
- Views must not query the database
- Controllers must not contain business logic
- Models must not know about HTTP (no `$_GET`, `$_POST` in models)

## Repository Pattern

Abstracts data access behind an interface.

```php
interface VehicleRepositoryInterface
{
    public function findById(int $id): ?Vehicle;
    public function findAll(): array;
    public function save(Vehicle $vehicle): void;
}

class EloquentVehicleRepository implements VehicleRepositoryInterface
{
    public function findById(int $id): ?Vehicle
    {
        return Vehicle::find($id);
    }
    // ...
}
```

Swap implementations (MySQL → Elasticsearch) without touching business logic.

## Dependency Injection

Inject dependencies instead of creating them inside classes.

```php
// BAD — hard to test, tightly coupled
class OrderService
{
    private $mailer;

    public function __construct()
    {
        $this->mailer = new SmtpMailer(); // hard dependency
    }
}

// GOOD — injectable, testable
class OrderService
{
    public function __construct(private readonly MailerInterface $mailer) {}
}
```
