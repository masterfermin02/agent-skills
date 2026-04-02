# When Clean Architecture Helps

Use stronger architecture when:
- domain rules are complex
- integrations are numerous
- business rules are long-lived
- testing core logic independently matters
- teams need safer change boundaries

Avoid heavy ceremony when:
- app is mostly CRUD
- MVP speed matters more than framework-independent purity
- abstractions would mostly wrap framework code without reducing pain
