#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import boto3




dynamodb = boto3.resource('dynamodb')


def get_next_seq(table, name):
    response = table.update_item(
        Key = {
                'name' : name
        },
        UpdateExpression = 'set seq = seq + :val',
        ExpressionAttributionValues = {
                ':val' : 1
        },
        ReturnValues = 'UPDATED_NEW'
        )
    return response['Attributes']['seq']
        

def lambda_handler(event, context):
   
    try:
            #get_sequence_data
            seqtable = dynamodb.Table('matchaSequence')
            nextseq = get_next_seq(seqtable,'matchaUserInfo')
            
            #get_data_inputonform
            param = json.loads(event['body'])
            username = param['username']
            userid = param['userid']
            email = param['email']
            age = param['age']
            height = param['height']
            
            # register_on_matchaUserInfo
            table = dynamodb.Table('matchaUserInfo')
            table.put_item(
                Item ={
                    'RegistrationID' : nextseq,
                    'username' : username,
                    'email' : email,
                    'age' : age,
                    'height' : height
                }
            )
            
            return {
                    "isBase64Encoded" : False,
                    "statusCode":200,
                    "headers": {
                        'Content-Type':'application/json',
                        'Access-Control-Allow-Headers':'Content-Type',
                        'Access-Control-Allow-Methods':'POST,GET',
                        'Access-Control-Allow-Origin':'*'
                    },
                        "body" : json.dumps({"result":"ok"})
                
            }
    except:
            import traceback
            traceback.print_exc()
            return{
                    'statusCode':500
            }