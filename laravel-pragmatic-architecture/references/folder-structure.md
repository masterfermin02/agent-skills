# Laravel Folder Structure

```text
app/
  Http/
    Controllers/
    Requests/
  Actions/
  Domain/
    Orders/
    Billing/
  Services/
    Integrations/
  Jobs/
  Policies/
  Support/
```

## Intent
- controllers stay thin
- Actions/Domain classes hold business workflows and rules
- external systems live in integration services
- Laravel remains idiomatic without stuffing everything into controllers/models
