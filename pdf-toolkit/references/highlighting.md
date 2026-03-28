# Highlighting

## Strategy
1. Use PyMuPDF (`fitz`) to open the PDF.
2. Search exact target phrases first.
3. If exact matching fails, search a shorter anchor phrase such as company name.
4. Add highlight annotations and save as a new file.

## Good targets
- employer names
- transfer descriptions
- exact deposit lines
- invoice ids
- dates with amounts when visible in one line

## Notes
- search results may return multiple rectangles per line; that is acceptable
- prefer visibly obvious highlighting over perfect minimal rectangles
- if exact highlighting is not possible, create a summary page or appendix as fallback
