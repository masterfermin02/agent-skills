# Laravel Pragmatic Rules

- do not put all business logic in controllers
- use Form Requests for input validation, not business decisions
- use Actions/Domain classes when workflows become important
- keep payment/order/subscription logic protected and testable
- stay idiomatic; do not recreate enterprise ceremony unless complexity truly demands it
