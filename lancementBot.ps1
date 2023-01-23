while(1){
    Write-Output "_______________________________________________________________________"
    Write-Output "
                                                                    
    __________       ___.   .__                        
    \______   \_____ \_ |__ |  |   ____   ____   ____  
    |     ___/\__  \ | __ \|  |  /  _ \ /  _ \ /  _ \ 
    |    |     / __ \| \_\ \  |_(  <_> |  <_> |  <_> )
    |____|    (____  /___  /____/\____/ \____/ \____/ 
                    \/    \/                              "

    Write-Output "_______________________________________________________________________"
    Write-Output ""
    Write-Output "1 - Lancer le Bot Pabloooo (.py)"
    Write-Output "2 - Lancer le Bot Escobabar (.cpp)"
    Write-Output "_______________________________________________________________________"
    Write-Output ""
    $choixUtilisateur = read-host "Que souhaitez vous faire ? 1"
    Write-Output ""

    #lancement du bot Pabloooooo
    if ( $choixUtilisateur -eq 1 )
    {
        #a voir la localisation
        python pablooo.py
    }

    if ( $choixUtilisateur -eq 2 )
    {
        #a voir la localisation
        g++ main.cpp -o Escobabar
        ./Escobabar.exe
    }
}