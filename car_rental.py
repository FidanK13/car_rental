

while True:
      k = input('kateqoriyani daxil edin')
      if k not in ('b','d','w','q'):
            print('duzgun kateqoriya daxil edin')
            continue
      elif k=='q':
            break
      else:
            i = round(float(input('ilkin gostericini daxil edin (mille)')), 2)
            s = round(float(input('son gostericini daxil edin (mille)')), 2)
            g = int(input('gunlerin sayini daxil edin'))
            m = s - i
            print('gedilen mesafe: ', m)
            if k=='b':
                  borc=(g*40)+(m*0.25)
            elif k=='d':
                  daily_limit=g*100
                  if m<=daily_limit:
                        borc=g*60
                  else:
                        borc=(g*60)+((m-daily_limit)*0.25)
            else:
                  hefte=g/7
                  hefte_limit=hefte*900
                  hefte_orta_limit=hefte*1500
                  if m<=hefte_limit:
                        borc=hefte*190
                  elif hefte_limit<m<hefte_orta_limit:
                        borc=hefte*290
                  else:
                        borc=(hefte*200)+((m-hefte_orta_limit)*0.25)
      print('Sizin cari borcunuz: ', round(borc,1))




