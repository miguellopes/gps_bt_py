import time, serial
 
def main():
#variáveis para guardar as informações que nos interessam.
        lat=""
        lon=""
        ns=""
        ew=""
        nr_sats=""
        alti=""
        velocidade=""
        ser = serial.Serial(
            port='/dev/tty.CBTGPS32-SPPslave',# é o dispositivo que estou a usar muda de caso para caso
            baudrate=4800,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
 
        ser.open()#abrir a ligação com o dispositivo
        time.sleep(2)
        out = ""
 
        while 1 :
            out += ser.readline(1)# ler infos do dispositivo (ver informações sobre o protocolo)
 
            if out[:3] == '$GP' and out[len(out)-2:] == '\r\n':
                if(out[3:6] == 'RMC'):
                    divs = out.split(',')
 
                    lat = divs[3]
                    lon = divs[5]
                    ns = divs[4]
                    ew = divs[6]
                    time.sleep(5)              
 
                if(out[3:6] == 'VTG'):
                    divs = out.split(',')
                    velocidade = divs[7]
                if(out[3:6] == 'GGA'):
                    divs = out.split(',')
                    alti = divs[9]
                    nr_sats = divs[7]
                out = ""
            if(lat!="" and lon!="" and ns!="" and ew!="" and nr_sats!="" and alti!="" and velocidade!=""):
                print lat
                print lon
                print nr_sats
                print alti
                print velocidade
                lat=""
                lon=""
                ns=""
                ew=""
                nr_sats=""
                alti=""
                velocidade=""
 
        ser.close()
        return true;   
 
if __name__ == "__main__":
    main()
