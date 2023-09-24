# Xtractor

Xtractor is a Python tool for extracting useful information from HTML comments from a list of target URLs.

**Note**: This tool was originally created by [@mrxfact0r] and is now being shared with the community.

## Features:
- Extracts HTML comments from provided URLs.
- Outputs extracted comments to the console.

## Installation:

1. Clone the repository:
   git clone https://github.com/mrxfact0r/Xtractor.git
   cd Xtractor

Install the required dependencies:
pip install -r requirements.txt

## Usage:
Run the tool with the following command:
cat [Target Urls File] | python3 Xtractor.py: The URL from which you want to extract HTML comments.

## Example:
cat urls.txt | python3 Xtractor.py > Comments.txt or > Comments.txt
