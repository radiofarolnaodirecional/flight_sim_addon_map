def skyvector_to_decimal(coord):

    '''
    Convert skyvector coordinates to decimal
    '''

    # Divide a string da coordenada completa em latitude e longitude
    latitude = coord[:7]   # Primeiros 7 caracteres representam a latitude
    longitude = coord[7:]   # Restante representa a longitude

    # Função auxiliar para converter de DMS para decimal
    def dms_to_decimal(part):
        if 'S' in part or 'N' in part:
            direction = 'S' if 'S' in part else 'N'
            degrees = int(part[:2])
            minutes = int(part[2:4])
            seconds = int(part[4:6])
        elif 'W' in part or 'E' in part:
            direction = 'W' if 'W' in part else 'E'
            degrees = int(part[:3])
            minutes = int(part[3:5])
            seconds = int(part[5:7])
        else:
            raise ValueError("Formato de coordenada inválido")
        
        # convert to decimal
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        
        # negative if S or W
        if direction in ['S', 'W']:
            decimal = -decimal
        
        return decimal

    # separate convert latitude and longitude
    lat_decimal = dms_to_decimal(latitude)
    lon_decimal = dms_to_decimal(longitude)
    
    return lat_decimal, lon_decimal

print(skyvector_to_decimal('195107S0435702W'))
