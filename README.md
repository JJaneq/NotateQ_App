# NotateQ-API
**NotateQ-API** is a simple REST API for uploading, storing and downloading files from a server.

## Endpoints
### Upload a file
**Endpoint:** `POST /api/files/`\
**Request:** Form-Data\
**Required data:**\
`title` - The title of the note\
`description` - A short description of added note\
`category` - [WIP] Categories assigned to the note - leave empty for now\
`author` - [WIP] Author of the note\
`file` - The file being uploaded (must be.docx, .pdf or .txt)\
**Response:** 
```json
{
    "id": 4,
    "title": "Title",
    "description": "Some description",
    "category": null,
    "author": "JJaneq",
    "upload_date": "2025-04-01T16:06:23.509266Z",
    "file": "http://localhost:8080/media/store/files/some_note.docx",
    "downloads": 0
}
```
***Response Explanation***\
`id` - Identifier of the uploaded file. \
`title` - The title of the note.\
`description` - Description of added note.\
`category` - Categories assigned to the note (currently null).\
`author` - Author of the note.\
`upload_date` - Timestamp when the file was uploaded.\n
`file` - URL where the file can be accessed\
`downloads` - The number of times the file has been downloaded.

### Retrive information about all files
**Endpoint:** `GET /api/files`