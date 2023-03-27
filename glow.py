R,G,B = 210,0,0

def colormix():
  global R,G,B
  stat = 15
  if R >= 225:
      if R <= 255 and G >= 30:
          R -= stat
          G += stat
      else:
          R += stat
          G += stat
  else:
      if R < 225 and G >= 30 or G >= 0 and B > 0:
          if G >= 225 or R == 30:
              if G <= 255 and B >= 30 or G == 0 and B > 0:
                  if R == 30:
                      if G <= 30 and B <= 255:
                          if G == 0:
                              B -= stat
                          else:
                              G -= stat
                              B -= stat
                      else:
                          G -= stat
                          B += stat
                  else:
                      G -= stat
                      R -= stat
                      B += stat
              else:
                  R -= stat
                  G += stat
                  B += stat
          else:
              R -= stat
              G += stat
      else:
          R += stat

  return (R,G,B)