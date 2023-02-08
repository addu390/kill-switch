# Kill Switch Service (Work in Progress)

- The app `kill_switch` will eventually be a stand-alone django app.
- [Django Installable Guide](https://realpython.com/installable-django-app/)

The basic idea of the "kill-switch" is to take a JSON input and evaluate a set of rules on the input JSON and return the match result (Boolean).

## Example:
- JSON input:
```
{
	"WORKFLOW": "PURCHASE",
	"BANK": "RBC"
}
```

- Predefined Rule: `WORKFLOW == "PURCHASE" and BANK == "RBC"`
- Output: `True`

![Validate True](./screenshots/validate-true.png)

- Predefined Rule: `WORKFLOW == "REFUND" and BANK == "RBC"`
- Output: `False`

![Validate False](./screenshots/validate-false.png)

While implementing a simple rule engine for the given JSON is quite easy, the expectation is that most APIs in the backend application would need to call the Kill-switch service to evaluate. Hence, ensuring low latency is of a higher priority.

The rest is a Work in Progress.