# C# Folder Structure

```text
src/
  Api/
    Controllers/
  Application/
    Orders/
    Payments/
  Domain/
    Orders/
    Billing/
  Infrastructure/
    Persistence/
    Integrations/
  Jobs/
  Shared/
```

## Intent
- controllers stay transport-focused
- Application coordinates workflows
- Domain holds important business rules
- Infrastructure handles DB and third-party systems
