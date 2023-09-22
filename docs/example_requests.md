# API Reference of OpenAI

Official document: https://platform.openai.com/docs/api-reference

## Chat Completion

Request:

```bash
curl -H "Content-Type: application/json" \
     -H "Authorization: Bearer $OPENAI_API_KEY" \
     -X POST \
     -d '{"model": "gpt-3.5-turbo-0301", "messages": [{"role": "user", "content": 
"hello"}]}' \
     https://api.openai.com/v1/chat/completions
```

Response:

```bash
{
  "id": "chatcmpl-81b0NnL4B06urJdKYelpkB8l2QgVI",
  "object": "chat.completion",
  "created": 1695391267,
  "model": "gpt-3.5-turbo-0301",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 9,
    "total_tokens": 18
  }
}
```

## Valid Models

Request:

```bash
url https://api.openai.com/v1/models \                                                                                                           base
-H "Authorization: Bearer $OPENAI_API_KEY"
```

Response:

```bash
{
  "object": "list",
  "data": [
    {
      "id": "gpt-4",
      "object": "model",
      "created": 1687882411,
      "owned_by": "openai",
      "permission": [
        {
          "id": "modelperm-6FFWHA4eLhaNkkCaNQYiVryW",
          "object": "model_permission",
          "created": 1695226861,
          "allow_create_engine": false,
          "allow_sampling": false,
          "allow_logprobs": false,
          "allow_search_indices": false,
          "allow_view": false,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "gpt-4",
      "parent": null
    },
    # and so on ...
  ]
}
```

## Files

### Upload
Request for upload files:

```bash
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F purpose="fine-tune" \
  -F file="@mydata.jsonl"
```

Response:

```bash
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 140,
  "created_at": 1613779121,
  "filename": "mydata.jsonl",
  "purpose": "fine-tune",
  "status": "uploaded" | "processed" | "pending" | "error"
}
```

### Get the list of files
Request:

```bash
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

Response:

```bash
{
  "object": "list",
  "data": [
    {
      "object": "file",
      "id": "file-cJBTT0amnPbXYabeEesxH4wD",
      "purpose": "fine-tune-results",
      "filename": "step_metrics.csv",
      "bytes": 12754,
      "created_at": 1695286512,
      "status": "processed",
      "status_details": null
    },
    {
      "object": "file",
      "id": "file-wDmwdokRvIEsbrxtZhS9svDO",
      "purpose": "fine-tune",
      "filename": "file",
      "bytes": 113989,
      "created_at": 1695285278,
      "status": "processed",
      "status_details": null
    },
    {
      "object": "file",
      "id": "file-cxd8eOF7hmnz9APOMo0gq303",
      "purpose": "fine-tune",
      "filename": "file",
      "bytes": 115015,
      "created_at": 1695285274,
      "status": "processed",
      "status_details": null
    }
  ]
}
```

### Delete a file

### Retrieve a file

## Fine-tuning

### Create a fine-tune Job

Request:

```bash
curl https://api.openai.com/v1/fine_tuning/jobs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d "{
    \"training_file\": "$FileID"
    \"model\": \"gpt-3.5-turbo\",
  }"
```

#### Status of a fine-tune job

Request:

```bash
curl https://api.openai.com/v1/fine_tuning/jobs/$JobID/events \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

#### Get the list of fine-tune jobs

Request:

```bash
curl https://api.openai.com/v1/fine_tuning/jobs?limit=2 \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

Response:

```bash
{"object":"list","data":[{"object":"fine_tuning.job","id":"ftjob-fWdzdTBqdCeO694DBCCSQlkK","model":"gpt-3.5-turbo-0613","created_at":1695285360,"finished_at":1695286509,"fine_tuned_model":"ft:gpt-3.5-turbo-0613:personal:recipe-ner:819klqSI","organization_id":"org-Swuf9P8k6yQVnVPhe2JzNtvK","result_files":["file-cJBTT0amnPbXYabeEesxH4wD"],"status":"succeeded","validation_file":"file-wDmwdokRvIEsbrxtZhS9svDO","training_file":"file-cxd8eOF7hmnz9APOMo0gq303","hyperparameters":{"n_epochs":3},"trained_tokens":91476,"error":null}],"has_more":false}
```

#### Cancel a fine-tune job


