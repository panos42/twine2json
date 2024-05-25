import argparse
from bs4 import BeautifulSoup
import json

def twine_html_to_json(html_file, json_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
    passages = soup.find_all('tw-passagedata')
    story = {}
    
    for passage in passages:
        pid = passage.get('pid')
        name = passage.get('name')
        text = passage.text
        story[pid] = {
            'name': name,
            'text': text
        }
    
    json_story = json.dumps(story, indent=4)
    
    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json_story)
    
    print(f"JSON story saved to {json_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert Twine HTML to JSON.")
    parser.add_argument('html_file', type=str, help='Path to the Twine HTML file')
    parser.add_argument('json_file', type=str, help='Path to save the JSON output file')

    args = parser.parse_args()
    
    twine_html_to_json(args.html_file, args.json_file)

if __name__ == "__main__":
    main()
