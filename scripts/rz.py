#!/usr/bin/env python3

import sys
import os
import shutil

RZ_DIR = './.releasezri'
TEMPLATE_FILE = './.releasezri/template.md'
CHANGELOG_FILE = './CHANGELOG.md'
TMP_DIR = './.tmprz'
RELEASE_NOTE_FILE = './.tmprz/release_notes.md'
VERSION = ''

def apply_notes_to_template(note):
    md = ''
    with open(TEMPLATE_FILE, 'r') as tf:
        md = tf.read() \
                    .replace('{RZ_VERSION}', VERSION) \
                    .replace('{RZ_CHANGELOG}', note)
    return md

def parse_release_note():
    note = ''
    collect = False
    updated_changelog = ''

    with open(CHANGELOG_FILE, 'r') as cf:
        for line in cf:
            if '## Unreleased' in line:
                collect = True
                continue
            if '## v' in line:
                break
            if collect:
                note += line
    return note

def save_release_note(note):
    os.makedirs(TMP_DIR, exist_ok = True)

    with open(RELEASE_NOTE_FILE, 'w') as rf:
        rf.write(note)

def update_changelog():
    updated_changelog = ''
    with open(CHANGELOG_FILE, 'r') as cf:
        updated_changelog = cf.read().replace('## Unreleased', '## ' + VERSION)

    with open(CHANGELOG_FILE, 'w') as cf:
        cf.write(updated_changelog)

def create_note():
    print('INFO: Preparing release notes...')
    note = parse_release_note()
    print('---- Release note for %s (parsed) ----' % VERSION)
    print(note)
    print('----')

    if note == '':
        print('ERROR: No changelog.')
        sys.exit(1)

    note = apply_notes_to_template(note)
    print('---- Release note for %s (applied to template) ----' % VERSION)
    print(note)
    print('----')
    save_release_note(note)

    print('INFO: Updating change log...')
    update_changelog()

    print('OK: All done. Run "cleanup" command after using release note.')

def cleanup():
    shutil.rmtree(TMP_DIR)
    print('OK: All done.')

def print_art():
    print('''
    ____       __                  _____        _
   / __ \___  / /__  ____ ________/__  /  _____(_)
  / /_/ / _ \/ / _ \/ __ `/ ___/ _ \/ /  / ___/ /
 / _, _/  __/ /  __/ /_/ (__  )  __/ /__/ /  / /
/_/ |_|\___/_/\___/\__,_/____/\___/____/_/  /_/
    ''')

if __name__ == '__main__':
    print_art()
    if len(sys.argv) < 2:
        print('ERROR: Missing command (create or cleanup)')
        sys.exit(1)

    command = sys.argv[1]

    if command == 'create':
        if len(sys.argv) < 3:
            print('ERROR: Missing version argument')
            sys.exit(1)
        VERSION = 'v' + sys.argv[2]
        create_note()

    elif command == 'cleanup':
        cleanup()

    else:
        print('ERROR: Invalid command!')
