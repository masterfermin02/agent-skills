# Node.js Folder Structure

```text
src/
  app/
  modules/
    orders/
    users/
    payments/
  domain/
  integrations/
  db/
  jobs/
  shared/
```

## Intent
- controllers stay thin
- modules own feature-level API flow
- domain owns business rules
- integrations wrap external systems
- repositories isolate persistence
