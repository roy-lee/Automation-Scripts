#!/bin/bash
FILEID="1JL6zBHgrQP0xJRR_fDBPu7R3txqRpQKu"
FILENAME="train_msra.tar.gz"
TOKEN="ya29.a0AfH6SMDPUKrOhaiUNb-1JWrRaXXcwDWb_nbBN8nPAYaftM6pB9z9t07sFqBuzGDde4nm_Zz5Ra2A2WJyzkV37FJMvmFTrjA7xNRqS3MT0Sj65CHU6MAHj8dtrXzNECSzFACvx6CE9LQBKwph35bulhXi03XmK5kJUoA"

curl --retry 999 --retry-delay 5000 -C - -H "Authorization: Bearer ${TOKEN}" https://www.googleapis.com/drive/v3/files/${FILEID}?alt=media -o ${FILENAME}