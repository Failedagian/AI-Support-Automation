# AI Support Automation - Copilot Instructions

## Project Overview
This is a Python-based support ticket automation system that routes customer support queries to appropriate automated responses based on keyword matching. The script processes customer tickets stored in CSV format and generates intelligent auto-responses.

## Architecture & Data Flow

### Core Components
- **Ticket Data**: Customer support tickets loaded into a Pandas DataFrame with columns: `TicketID`, `CustomerName`, `Query`
- **Response Engine**: `auto_response()` function implements rule-based routing using keyword detection
- **I/O Pipeline**: Reads from `tickets.csv`, processes tickets, outputs `tickets_with_responses.csv`

### Pattern: Keyword-Based Routing
The `auto_response()` function uses cascading `if-elif` logic to match keywords in customer queries and return templated responses:
```python
if "password" in query:
    return "Please reset your password using 'Forgot Password'."
```
When adding new response types, follow this pattern by adding new keyword checks before the fallback `else` clause.

## Key Workflows

### Processing Support Tickets
1. Load sample data into DataFrame (or read from existing CSV)
2. Apply `auto_response()` to each ticket's `Query` field
3. Save enriched DataFrame with new `Response` column to CSV output

### Testing Approach
- Modify the `data` dictionary to test new query types
- Verify responses are accurate before scaling to production data
- Check CSV output files for formatting and correctness

## Development Patterns

### Adding New Response Types
1. Identify new keyword patterns in customer queries
2. Add new `elif` clause in `auto_response()` with appropriate keyword checks
3. Keep response templates concise and actionable (e.g., direct customers to self-service options)
4. Update sample `data` to include test cases for the new pattern

### Extending the System
- For more complex routing, consider adding a configuration dictionary mapping keywords to response templates
- Current approach works well for <10 response types; if exceeding this, refactor to table-driven design
- Avoid modifying the CSV I/O logic unless handling new data sources

## Dependencies
- `pandas`: DataFrame manipulation and CSV I/O

## Common Tasks
- **Run the script**: `python "AI  support Automation.py"`
- **Inspect ticket data**: Check generated `tickets_with_responses.csv`
- **Add response patterns**: Modify `auto_response()` function with new keyword-response pairs
