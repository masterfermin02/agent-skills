# Usage

## Typical tasks
- merge monthly bank statements in a strict order
- replace a weak source PDF with a cleaner export
- produce one final file for visa upload
- generate a highlighted version showing employer income entries

## Default output directory
`/home/forge/.openclaw/workspace/merged/`

## Safety
- never overwrite source files
- create a new output file instead of mutating originals unless explicitly requested
- preserve the original order given by the user

## Example asks
- merge these in this order: dec, jan, feb, then online banking
- replace the last PDF with this cleaner one
- highlight all transactions that say CREDIQUE
- make this visa-ready
