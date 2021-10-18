# TSV_to_json

TSV to json is a parser to convert files with the format TSV (Tabulation-separated values) to JSON (Javascript Object Notation).

## Usage
Specify the input TSV file you want to convert by replacing "jpn_eng_sentences.tsv" in the app.py script.

```python
old_data_lines =  open('jpn_eng_sentences.tsv', encoding='utf8').read().split('\n')
```
The output file is named "parsed_data.txt" and will be created in the same folder where you executed the script.

You can change the name of the output file by editing "parsed_data.txt" with the name of your choice.

```python
with open('parsed_data.txt', 'w', encoding='utf8') as outfile:
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
