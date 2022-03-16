# cryptoMLBOT

#停止しない自動売買ボットの作り方。python 3

#自動売買ボットはいろいろな原因(バグ、API変更、サーバーリソースなど)で良く停止しますが、停止したまま気づかないと、大きく損失したりします。
#python3で停止しないボットの作り方です。

#方針
#ヘルスチェックを使います。一定時間ごとにボットの状態が正常であることを報告し、一定時間報告がなければ再起動させます。正常かどうかは、データが最新か、最後にループが回った時刻が最近#か、などで判断します。
