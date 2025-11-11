thonimport os
import json
from extractors.instagram_parser import parse_instagram_data
from outputs.exporters import export_to_json
from config.settings import SETTINGS

def main():
    instagram_profile_url = SETTINGS['INSTAGRAM_PROFILE_URL']
    session_id = SETTINGS['SESSION_ID']

    # Parse Instagram profile data
    profile_data = parse_instagram_data(instagram_profile_url, session_id)

    # Export parsed data to JSON
    export_to_json(profile_data, 'output.json')

if __name__ == "__main__":
    main()