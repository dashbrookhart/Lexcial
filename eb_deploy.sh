eb init group-05-Lexical-app --region us-west-2 --platform Docker --key $PEM_NAME
eb create group-05-Lexical-env --verbose --envvars AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --envvars AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
