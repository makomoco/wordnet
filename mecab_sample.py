# -*- coding: utf-8 -*-

import MeCab

sentence = 'AWSの有名なサービスにAmazon Elastic Compute Cloud (EC2) とAmazon Simple Storage Service (S3) がある。
これまでのクライアントが保有していた物理的なサーバファームと比較してAWSは大規模な計算処理能力を速やかに提供出来ることが強みである。'

t = MeCab.Tagger('')
print(t.parse(sentence))