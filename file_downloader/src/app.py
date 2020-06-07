
import pickle
import os.path
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

creds = None
credentialsFile = "C:\\Users\\dbhakuni\\credentials.json"
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(credentialsFile, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

flow = InstalledAppFlow.from_client_secrets_file(credentialsFile, SCOPES)
creds = flow.run_local_server(port=0)
with open('token.pickle', 'wb') as token:
    pickle.dump(creds, token)

drive_service = build('drive', 'v3', credentials=creds)
file_id = '1kGbhAWlrFZygnTCrrxLMVHVeeneVZ1yz'
request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
