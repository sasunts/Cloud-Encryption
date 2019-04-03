from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import io
import auth
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'

authIntsance = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials  =authIntsance.get_credentials()
http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

def listFiles():

    results = drive_service.files().list(
        pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))


def uploadFile(fileName, filePath):
    file_metadata = {'name': fileName}
    media = MediaFileUpload(filePath,
                            mimetype="text/plain")
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    fileID = file.get('id')
    print('File ID: ' + fileID )


def downloadFile(file_id, writePath):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(writePath, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())
