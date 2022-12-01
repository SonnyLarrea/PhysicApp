import flet
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from flet.matplotlib_chart import MatplotlibChart
from flet import AppBar, ElevatedButton, Page, Text, View, colors, Dropdown, dropdown, RadioGroup, Column, Radio, TextField , IconButton, icons, Image, theme
from flet import Markdown
from funciones_calculo import mru_calcular_posicio_final, mru_calcular_posicio_inicial, mru_calcular_temps, mru_calcular_velocitat
from funciones_calculo import forca_calcular_acceleracio, forca_calcular_forca, forca_calcular_massa
from funciones_calculo import ep_calcular_altura, ep_calcular_ep, ep_calcular_massa, ep_calcular_gravetat
from funciones_calculo import ec_calcular_ec, ec_calcular_massa, ec_calcular_velocitat, calcular_x, forca_fregament_calcular_ff
from funciones_calculo import ff_calcular_coeficient_friccio, ff_calcular_normal, intensitat_camp_calcul, ic_calcular_forca, ic_calcular_massa
from funciones_calculo import energia_mecanica_calcul, em_calcular_ec, em_calcular_ep, camp_gravitatori_calcul, cg_calcul_massa, cg_calcul_distancia
from funciones_calculo import ep_gravitatoria_calcul, epg_calcular_massa_1, epg_calcular_massa_2, epg_calcular_distancia 
from funciones_calculo import gu_calcular_forca_atraccio, gu_calcular_massa_1, gu_calcular_massa_2, gu_calcular_r

matplotlib.use("svg")
plt.style.use("fivethirtyeight")
def main(page: Page):
    image=Image(src=f"/imagenes/3671320.jpg", 
    fit="fitWidth",
    height=400
    )
    page.theme_mode="dark"
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        title=Text("PhysicApp", size=50, color=colors.PINK_600, ), 
                        bgcolor=colors.SURFACE_VARIANT, center_title=True,
                    ),
                    image, dd1, dd2, b
                ]
            )
        )
        if page.route == "/MRU":
            page.views.append(
                View(
                    "/MRU",
                    [
                        AppBar(title=Text("MRU", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Tornar enrere", on_click=lambda _: page.go("/")),
                        mru_image, mru_text_1, mru_selection, mru_posicio_inicial, mru_posicio_final, mru_temps, mru_velocitat, mru_calcular, mru_resultat
                    ],
                )
            )
        elif page.route == "/Força":
            page.views.append(
                View(
                    "/Força",
                    [
                        AppBar(title=Text("Força", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        forca_image, forca_text_1, forca_selection, forca_f, forca_massa, forca_acceleracio, forca_calcular, forca_resultat
                    ],
                )
            )
        elif page.route == "/Energia potencial":
            page.views.append(
                View(
                    "/Energia potencial",
                    [
                        AppBar(title=Text("Energia potencial", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ep_image, ep_text_1, ep_selection, energia_potencial, ep_massa, ep_gravetat, ep_altura, ep_calcular, ep_resultat
                    ],
                )
            )
        elif page.route == "/Energia cinetica":
            page.views.append(
                View(
                    "/Energia cinetica",
                    [
                        AppBar(title=Text("Energia cinetica", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ec_image, ec_text_1, ec_selection, energia_cinetica, ec_massa, ec_velocitat, ec_calcular, ec_resultat
                    ],
                )
            )
        elif page.route == "/MRUA":
            page.views.append(
                View(
                    "/MRUA",
                    [
                        AppBar(title=Text("MRUA", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        mrua_image, mrua_column_1, mrua_grafica
                    ], scroll="always"
                )
            )
        elif page.route == "/Força de fregament":
            page.views.append(
                View(
                    "/Força de fregament",
                    [
                        AppBar(title=Text("Força de fregament", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT,
                         leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ff_image, forca_fregament_text_1, forca_fregament_selection, forca_fregament, forca_fregament_coeficient_friccio, 
                        forca_fregament_f_normal, forca_fregament_calcular, forca_fregament_resultat
                    ]
                )
            )
        elif page.route == "/Intensitat de camp":
            page.views.append(
                View(
                    "/Intensitat de camp",
                    [
                        AppBar(title=Text("Intensitat de camp", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ic_image, intensitat_camp_text_1, intensitat_camp_selection, intensitat_camp, ic_forca, ic_massa, 
                        intensitat_camp_calcular, ic_resultat
                    ]
                )
            )
        elif page.route == "/Energia mecanica":
            page.views.append(
                View(
                    "/Energia mecanica",
                    [
                        AppBar(title=Text("Energia mecanica", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT,
                         leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        em_image, energia_mecanica_text_1, energia_mecanica_selection, energia_mecanica, em_ec, em_ep, 
                        energia_mecanica_calcular, em_resultat
                    ]
                )
            )
        elif page.route == "/Camp gravitatori":
            page.views.append(
                View(
                    "/Camp gravitatori",
                    [
                        AppBar(title=Text("Camp gravitatori", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        cg_image, camp_gravitatori_text_1, camp_gravitatori_text_2, camp_gravitatori_text_3,camp_gravitatori_text_4,
                         camp_gravitatori_selection, camp_gravitatori, cg_distancia, cg_massa, cg_calcular, cg_resultat
                    ]
                )
            )
        elif page.route == "/Energia potencial gravitatoria":
            page.views.append(
                View(
                    "/Energia potencial gravitatoria",
                    [
                        AppBar(title=Text("Energia potencial gravitatoria", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT, 
                        leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        epg_image, ep_gravitatoria_text_1, ep_gravitatoria_selection, ep_gravitatoria, epg_massa_1, epg_massa_2, epg_distancia, 
                        ep_gravitatoria_calcular, epg_resultat
                    ]
                )
            )
        elif page.route == "/Llei de la gravitació universal":
            page.views.append(
                View(
                    "/Llei de la gravitació universal",
                    [
                        AppBar(title=Text("Llei de la gravitació universal", size=50, weight=flet.FontWeight.BOLD), center_title=True, bgcolor=colors.SURFACE_VARIANT,
                         leading=flet.Icon(icons.CALCULATE_OUTLINED, size=40)),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        gu_image, gravitacio_universal_text_1, gravitacio_universal_selection, forca_atraccio, gu_massa_1, gu_massa_2, gu_distancia,
                        gravitacio_universal_calcular, gu_resultat
                    ]
                )
            )
        page.update()

    def dropdown1_changed(e):
        dd2.visible = True
        if dd1.value == "Dinamica":
            dd2.options = [
                dropdown.Option("Força"),
                dropdown.Option("Força de fregament")
            ]
        elif dd1.value == "Treball i energia":
            dd2.options = [
                dropdown.Option("Energia potencial"),
                dropdown.Option("Energia cinetica"),
                dropdown.Option("Energia mecanica")
            ]
        elif dd1.value == "Camp gravitatori":
            dd2.options = [
                dropdown.Option("Intensitat de camp"),
                dropdown.Option("Llei de la gravitació universal"),
                dropdown.Option("Camp gravitatori"),
                dropdown.Option("Energia potencial gravitatoria")
            ]
        elif dd1.value == "Cinematica":
            dd2.options = [
                dropdown.Option("MRU"),
                dropdown.Option("MRUA")
            ]
        page.update()

    dd1 = Dropdown(
        width=300, on_change=dropdown1_changed, border_color=colors.PINK_600,
        options=[
            dropdown.Option("Cinematica"),
            dropdown.Option("Dinamica"),
            dropdown.Option("Treball i energia"),
            dropdown.Option("Camp gravitatori")
        ],
    )

    def dropdown2_changed(e):
        b.visible = True 
        page.update()
    
    dd2 = Dropdown(width=300, visible=False, on_change=dropdown2_changed, border_color=colors.WHITE)
    def button_clicked(e):
        selection = "/" + dd2.value
        page.go(selection)
        page.update()
    b = ElevatedButton(text="Continua", on_click=button_clicked, visible=False)
    
    #VISTA MRU
   
    mru_image = Image(src=f"/imagenes/mru.png")

    def mru_radiogroup_changed(e):
        if mru_selection.value == "posicio final":
            mru_posicio_inicial.visible = True
            mru_velocitat.visible = True
            mru_temps.visible = True
            mru_posicio_final.visible = False
        elif mru_selection.value == "velocitat":
            mru_posicio_inicial.visible = True
            mru_velocitat.visible = False
            mru_temps.visible = True
            mru_posicio_final.visible = True
        elif mru_selection.value == "temps":
            mru_posicio_inicial.visible = True
            mru_velocitat.visible = True
            mru_temps.visible = False
            mru_posicio_final.visible = True
        elif mru_selection.value == "posicio inicial":
            mru_posicio_inicial.visible = False
            mru_velocitat.visible = True
            mru_temps.visible = True
            mru_posicio_final.visible = True
        mru_calcular.visible = True

        page.update()

    mru_text_1 = Text("Que vols calcular d'un MRU?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    mru_selection = RadioGroup(content=Column([
        Radio(value="velocitat", label="Velocitat"),
        Radio(value="posicio inicial", label="Posició inicial"),
        Radio(value="temps", label="Temps"),
        Radio(value="posicio final", label="Posició final")]), on_change=mru_radiogroup_changed)
    
    def button_clicked_mru(e):
        if mru_selection.value == "posicio final":
            posicio_final = mru_calcular_posicio_final(float(mru_posicio_inicial.value), 
                float(mru_velocitat.value), float(mru_temps.value))
            mru_resultat.value = "La posició final de l'objecte és " + str(posicio_final) + "m"
        elif mru_selection.value == "posicio inicial":
            posicio_inicial = mru_calcular_posicio_inicial(float(mru_posicio_final.value), 
                float(mru_velocitat.value), float(mru_temps.value))
            mru_resultat.value = "La posició inicial de l'objecte és " + str(posicio_inicial) + "m"
        elif mru_selection.value == "temps":
            temps = mru_calcular_temps(posicio_inicial=float(mru_posicio_inicial.value),
                velocitat=float(mru_velocitat.value), posicio_final=float(mru_posicio_final.value))
            mru_resultat.value = "El temps de l'objecte és " + str(temps) + "s"
        elif mru_selection.value == "velocitat":
            velocitat = mru_calcular_velocitat(float(mru_posicio_inicial.value), 
                float(mru_posicio_final.value), float(mru_temps.value))
            mru_resultat.value = "La velocitat de l'objecte és " + str(velocitat) + "m/s"
        

        mru_resultat.visible = True

        page.update()
    mru_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_mru, visible=False)
    

    mru_posicio_inicial = TextField(label="Posició inicial", visible=False, width=300)
    mru_posicio_final = TextField(label="Posició final", visible=False, width=300)
    mru_temps = TextField(label="Temps", visible=False, width=300)
    mru_velocitat = TextField(label="Velocitat", visible=False, width=300)

    mru_resultat = Text(visible=False)

    #VISTA FORÇA

    forca_image = Image(src=f"/imagenes/forca.png")

    def forca_radiogroup_changed(e):
        if forca_selection.value == "forca":
           forca_f.visible = False
           forca_acceleracio.visible = True
           forca_massa.visible = True
        elif forca_selection.value == "massa":
            forca_f.visible = True
            forca_acceleracio.visible = True
            forca_massa.visible = False
        elif forca_selection.value == "acceleracio":
            forca_f.visible = True
            forca_acceleracio.visible = False
            forca_massa.visible = True
        forca_calcular.visible = True
        page.update()

    forca_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    forca_selection = RadioGroup(content=Column([
        Radio(value="forca", label="Força"),
        Radio(value="massa", label="Massa"),
        Radio(value="acceleracio", label="Acceleració")]), on_change=forca_radiogroup_changed)

    def button_clicked_forca(e):
        if forca_selection.value == "forca":
            forca_total = forca_calcular_forca(massa=float(forca_massa.value), 
                acceleracio=float(forca_acceleracio.value))
            forca_resultat.value = "La força que fa l'objecte és " + str(forca_total) + "N"
        elif forca_selection.value == "massa":
            massa = forca_calcular_massa(forca=float(forca_f.value), 
                acceleracio=float(forca_acceleracio.value))
            forca_resultat.value = "La massa de l'objecte és " + str(massa) + "kg"
        elif forca_selection.value == "acceleracio":
            acceleracio = forca_calcular_acceleracio(forca=float(forca_f.value),
                massa=float(forca_massa.value))
            forca_resultat.value = "L'acceleració de l'objecte és " + str(acceleracio) + "m/s2"
        forca_resultat.visible = True

        page.update()
    forca_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_forca, visible=False)
    
    forca_f = TextField(label="Força", visible=False, width=300)
    forca_massa = TextField(label="Massa", visible=False, width=300)
    forca_acceleracio = TextField(label="Acceleració", visible=False, width=300)
    forca_resultat = Text(visible=False)

    #ENERGIA POTENCIAL

    ep_image = Image(src=f"/imagenes/ep.png")

    def ep_radiogroup_changed(e):
        if ep_selection.value == "energia_potencial":
           energia_potencial.visible = False
           ep_massa.visible = True
           ep_gravetat.visible = True
           ep_altura.visible = True
        elif ep_selection.value == "massa":
           energia_potencial.visible = True
           ep_massa.visible = False
           ep_gravetat.visible = True
           ep_altura.visible = True
        elif ep_selection.value == "gravetat":
           energia_potencial.visible = True
           ep_massa.visible = True
           ep_gravetat.visible = False
           ep_altura.visible = True
        elif ep_selection.value == "altura":
           energia_potencial.visible = True
           ep_massa.visible = True
           ep_gravetat.visible = True
           ep_altura.visible = False
        ep_calcular.visible = True
        page.update()

    ep_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    ep_selection = RadioGroup(content=Column([
        Radio(value="energia_potencial", label="Energia potencial"),
        Radio(value="massa", label="Massa"),
        Radio(value="gravetat", label="Gravetat"),
        Radio(value="altura", label="Altura")]), on_change=ep_radiogroup_changed)

    def button_clicked_ep(e):
        if ep_selection.value == "energia_potencial":
            ep_total = ep_calcular_ep(massa=float(ep_massa.value), 
                gravetat=float(ep_gravetat.value), altura=float(ep_altura.value))
            ep_resultat.value = "L'energia potencial que té l'objecte és " + str(ep_total) + "J"
        elif ep_selection.value == "massa":
            massa = ep_calcular_massa(energia_potencial=float(energia_potencial.value), 
                gravetat=float(ep_gravetat.value), altura=float(ep_altura.value))
            ep_resultat.value = "La massa de l'objecte és " + str(massa) + "kg"
        elif ep_selection.value == "gravetat":
            gravetat = ep_calcular_gravetat(energia_potencial=float(energia_potencial.value),
                massa=float(ep_massa.value), altura=float(ep_altura.value))
            ep_resultat.value = "La gravetat de l'objecte és " + str(gravetat) + "m/s2"
        elif ep_selection.value == "altura":
            altura = ep_calcular_altura(energia_potencial=float(energia_potencial.value),
                massa=float(ep_massa.value), gravetat=float(ep_gravetat.value))
            ep_resultat.value = "L'altura de l'objecte és " + str(altura) + "m"
        ep_resultat.visible = True

        page.update()
    ep_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_ep, visible=False)
    
    energia_potencial = TextField(label="Energia potencial", visible=False, width=300)
    ep_massa = TextField(label="Massa", visible=False, width=300)
    ep_gravetat = TextField(label="Gravetat", visible=False, width=300)
    ep_altura = TextField(label="Altura", visible=False, width=300)
    ep_resultat = Text(visible=False)

    #VISTA ENERGIA CINETICA

    ec_image = Image(src=f"/imagenes/ec.png")

    def ec_radiogroup_changed(e):
        if ec_selection.value == "energia_cinetica":
           energia_cinetica.visible = False
           ec_massa.visible = True
           ec_velocitat.visible = True
        elif ec_selection.value == "massa":
           energia_cinetica.visible = True
           ec_massa.visible = False
           ec_velocitat.visible = True
        elif ec_selection.value == "velocitat":
           energia_cinetica.visible = True
           ec_massa.visible = True
           ec_velocitat.visible = False
        ec_calcular.visible = True
        page.update()

    ec_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    ec_selection = RadioGroup(content=Column([
        Radio(value="energia_cinetica", label="Energia cinetica"),
        Radio(value="massa", label="Massa"),
        Radio(value="velocitat", label="Velocitat")]), on_change=ec_radiogroup_changed)

    def button_clicked_ec(e):
        if ec_selection.value == "energia_cinetica":
            ec = ec_calcular_ec(massa=float(ec_massa.value), 
                velocitat=float(ec_velocitat.value))
            ec_resultat.value = "L'energia cinetica que té l'objecte és " + str(ec) + "J"
        elif ec_selection.value == "massa":
            massa = ec_calcular_massa(energia_cinetica=float(energia_cinetica.value), 
                velocitat=float(ec_velocitat.value))
            ec_resultat.value = "La massa de l'objecte és " + str(massa) + "kg"
        elif ec_selection.value == "velocitat":
            velocitat = ec_calcular_velocitat(energia_cinetica=float(energia_cinetica.value),
                massa=float(ec_massa.value))
            ec_resultat.value = "La gravetat de l'objecte és " + str(velocitat) + "m/s2"
        ec_resultat.visible = True

        page.update()
    ec_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_ec, visible=False)

    energia_cinetica = TextField(label="Energia cinetica", visible=False, width=300)
    ec_massa = TextField(label="Massa", visible=False, width=300)
    ec_velocitat = TextField(label="Velocitat", visible=False, width=300)
    ec_resultat = Text(visible=False)

    #VISTA MRUA

    mrua_image = Image(src=f"/imagenes/mrua.png")

    mrua_text_1 = Text("ATENCIÓ! Si només tens un cos introdueix 0 en totes les caselles del segon cos.", 
    size=20, weight=flet.FontWeight.BOLD)
    mrua_text_2 = Text("Introdueix les dades per fer una grafica d'un MRUA", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    mrua_cos_1 = Text("Cos 1", style="titleMedium" )
    mrua_x0_1 = TextField(label="Posició inicial", visible=True, width=300)
    mrua_velocitat_1 = TextField(label="Velocitat", visible=True, width=300)
    mrua_acceleracio_1 = TextField(label="Acceleració", visible=True, width=300)
    mrua_cos_2 = Text("Cos 2", style="titleMedium" )
    mrua_x0_2 = TextField(label="Posició inicial", visible=True, width=300)
    mrua_velocitat_2 = TextField(label="Velocitat", visible=True, width=300)
    mrua_acceleracio_2 = TextField(label="Acceleració", visible=True, width=300)

    fig, axs = plt.subplots (1, 1, figsize=(9,6))
    mrua_grafica =  MatplotlibChart(fig, original_size=True)

    def button_clicked_mrua(e):
        
        step = 0.1
        temps = np.arange(0, 30, step)
        posicio_final_llista_1 = []
        posicio_final_llista_2 = []
        for t in temps:
            mrua_posicio_final_1 = calcular_x(x0=float(mrua_x0_1.value), v=float(mrua_velocitat_1.value), a=float(mrua_acceleracio_1.value), t=t)
            posicio_final_llista_1.append(mrua_posicio_final_1)
            mrua_posicio_final_2 = calcular_x(x0=float(mrua_x0_2.value), v=float(mrua_velocitat_2.value), a=float(mrua_acceleracio_2.value), t=t)
            posicio_final_llista_2.append(mrua_posicio_final_2)
        

        fig, axs = plt.subplots (1, 1, figsize=(9, 6))
        axs.plot(temps, posicio_final_llista_1)
        axs.plot(temps, posicio_final_llista_2)
        axs.set_xlim(0, 30)
        axs.set_xlabel("Temps")
        axs.set_ylabel("x")

        mrua_grafica.figure = fig
        mrua_grafica.update()
        page.update()
    mrua_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_mrua, visible=True)

    mrua_column_1 = flet.Column(spacing=0, controls=[mrua_text_1, mrua_text_2, mrua_cos_1, mrua_x0_1, mrua_velocitat_1, mrua_acceleracio_1, 
    mrua_cos_2, mrua_x0_2, mrua_velocitat_2, mrua_acceleracio_2, mrua_calcular])

   #VISTA FORÇA DE FREGAMENT

    ff_image = Image(src=f"/imagenes/ff.png")

    def forca_fregament_radiogroup_changed(e):
        if forca_fregament_selection.value == "forca_fregament":
           forca_fregament.visible = False
           forca_fregament_coeficient_friccio.visible = True
           forca_fregament_f_normal.visible = True
        elif forca_fregament_selection.value == "coeficient_friccio":
           forca_fregament.visible = True
           forca_fregament_coeficient_friccio.visible = False
           forca_fregament_f_normal.visible = True
        elif forca_fregament_selection.value == "forca_normal":
           forca_fregament.visible = True
           forca_fregament_coeficient_friccio.visible = True
           forca_fregament_f_normal.visible = False
        forca_fregament_calcular.visible = True
        page.update()

    forca_fregament_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    forca_fregament_selection = RadioGroup(content=Column([
        Radio(value="forca_fregament", label="Força de fregament"),
        Radio(value="coeficient_friccio", label="Coeficient de fricció"),
        Radio(value="forca_normal", label="Força normal")]), on_change=forca_fregament_radiogroup_changed)

    def button_clicked_forca_fregament(e):
        if forca_fregament_selection.value == "forca_fregament":
            forca_fregament_total = forca_fregament_calcular_ff(coeficient_friccio=float(forca_fregament_coeficient_friccio.value), 
                forca_normal=float(forca_fregament_f_normal.value))
            forca_fregament_resultat.value = "La força que fa l'objecte és " + str(forca_fregament_total) + "N"
        elif forca_fregament_selection.value == "coeficient_friccio":
            coeficient_friccio = ff_calcular_coeficient_friccio(forca_fregament=float(forca_fregament.value), 
                forca_normal=float(forca_fregament_f_normal.value))
            forca_fregament_resultat.value = "La massa de l'objecte és " + str(coeficient_friccio)
        elif forca_fregament_selection.value == "forca_normal":
            forca_normal = ff_calcular_normal(forca_fregament=float(forca_fregament.value),
                coeficient_friccio=float(forca_fregament_coeficient_friccio.value))
            forca_fregament_resultat.value = "L'acceleració de l'objecte és " + str(forca_normal) + "N"
        forca_fregament_resultat.visible = True

        page.update()
    forca_fregament_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_forca_fregament, visible=False)


    forca_fregament = TextField(label="Força de fregament", visible=False, width=300)
    forca_fregament_coeficient_friccio = TextField(label="Coeficient de fricció", visible=False, width=300)
    forca_fregament_f_normal = TextField(label="Força normal", visible=False, width=300)
    forca_fregament_resultat = Text(visible=False)
    
    #VISTA INTENSITAT DE CAMP

    ic_image = Image(src=f"/imagenes/ic.png")

    def intensitat_camp_radiogroup_changed(e):
        if intensitat_camp_selection.value == "intensitat_camp":
           intensitat_camp.visible = False
           ic_forca.visible = True
           ic_massa.visible = True
        elif intensitat_camp_selection.value == "forca":
           intensitat_camp.visible = True
           ic_forca.visible = False
           ic_massa.visible = True
        elif intensitat_camp_selection.value == "massa":
           intensitat_camp.visible = True
           ic_forca.visible = True
           ic_massa.visible = False
        intensitat_camp_calcular.visible = True
        page.update()

    intensitat_camp_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    intensitat_camp_selection = RadioGroup(content=Column([
        Radio(value="intensitat_camp", label="Intensitat de camp"),
        Radio(value="forca", label="Força"),
        Radio(value="massa", label="Massa")]), on_change=intensitat_camp_radiogroup_changed)

    def button_clicked_intensitat_camp(e):
        if intensitat_camp_selection.value == "intensitat_camp":
            intensitat_camp_final = intensitat_camp_calcul(forca=float(ic_forca.value), 
                massa=float(ic_massa.value))
            ic_resultat.value = "L'intensitat de camp del cos és " + str(intensitat_camp_final) + "m/s2"
        elif intensitat_camp_selection.value == "forca":
            forca = ic_calcular_forca(intensitat_camp=float(intensitat_camp.value), 
                massa=float(ic_massa.value))
            ic_resultat.value = "La força que exerceix el cos és " + str(forca) + "N"
        elif intensitat_camp_selection.value == "massa":
            massa = ic_calcular_massa(intensitat_camp=float(intensitat_camp.value),
                forca=float(ic_forca.value))
            ic_resultat.value = "La massa del cos és " + str(massa) + "kg"
        ic_resultat.visible = True

        page.update()
    intensitat_camp_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_intensitat_camp, visible=False)

    intensitat_camp = TextField(label="Intensitat de camp", visible=False, width=300)
    ic_forca = TextField(label="Força", visible=False, width=300)
    ic_massa = TextField(label="Massa", visible=False, width=300)
    ic_resultat = Text(visible=False)

    #VISTA ENERGIA MECANICA

    em_image = Image(src=f"/imagenes/em.png")

    def energia_mecanica_radiogroup_changed(e):
        if energia_mecanica_selection.value == "energia_mecanica":
           energia_mecanica.visible = False
           em_ec.visible = True
           em_ep.visible = True
        elif energia_mecanica_selection.value == "energia_cinetica":
           energia_mecanica.visible = True
           em_ec.visible = False
           em_ep.visible = True
        elif energia_mecanica_selection.value == "energia_potencial":
           energia_mecanica.visible = True
           em_ec.visible = True
           em_ep.visible = False
        energia_mecanica_calcular.visible = True
        page.update()

    energia_mecanica_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    energia_mecanica_selection = RadioGroup(content=Column([
        Radio(value="energia_mecanica", label="Energia mecanica"),
        Radio(value="energia_cinetica", label="Energia cinetica"),
        Radio(value="energia_potencial", label="Energia potencial")]), on_change=energia_mecanica_radiogroup_changed)

    def button_clicked_energia_mecanica(e):
        if energia_mecanica_selection.value == "energia_mecanica":
            em_total = energia_mecanica_calcul(ec=float(em_ec.value), 
                ep=float(em_ep.value))
            em_resultat.value = "L'energia mecànica total és de " + str(em_total) + "J"
        elif energia_mecanica_selection.value == "energia_cinetica":
            ec_total = em_calcular_ec(em=float(energia_mecanica.value), 
                ep=float(em_ep.value))
            em_resultat.value = "L'energia cinetica total és de " + str(ec_total) + "J"
        elif energia_mecanica_selection.value == "energia_potencial":
            ep_total = em_calcular_ep(em=float(energia_mecanica.value), 
                ec=float(em_ec.value))
            em_resultat.value = "L'energia potencial total és de " + str(ep_total) + "J"
        em_resultat.visible = True

        page.update()
    energia_mecanica_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_energia_mecanica, visible=False)

    energia_mecanica = TextField(label="Energia mecànica", visible=False, width=300)
    em_ec = TextField(label="Energia cinetica", visible=False, width=300)
    em_ep = TextField(label="Energia potencial", visible=False, width=300)
    em_resultat = Text(visible=False)

    #VISTA CAMP GRAVITATORI 

    cg_image = Image(src=f"/imagenes/cg.png")

    def camp_gravitatori_radiogroup_changed(e):
        if camp_gravitatori_selection.value == "intensitat_camp_gravitatori":
           camp_gravitatori.visible = False
           cg_massa.visible = True
           cg_distancia.visible = True
        elif camp_gravitatori_selection.value == "massa":
           camp_gravitatori.visible = True
           cg_massa.visible = False
           cg_distancia.visible = True
        elif camp_gravitatori_selection.value == "distancia":
           camp_gravitatori.visible = True
           cg_massa.visible = True
           cg_distancia.visible = False
        cg_calcular.visible = True
        page.update()

    camp_gravitatori_text_1 = Text("ATENCIO! Aquests càlculs són en mòdul.", size=20, weight=flet.FontWeight.BOLD)
    camp_gravitatori_text_2 = Text("La constant G sempre és: 6,67*10^-11", size=20, weight=flet.FontWeight.BOLD)
    camp_gravitatori_text_3 = Text(
    "IMPORTANT! Sempre que volguis utilitzar nombres grans, hauràs d'expresar-los de la següent manera re+/-n, exemple: 1.48e-10 o 1.48e+10 ", 
    size=20, weight=flet.FontWeight.BOLD)
    camp_gravitatori_text_4 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    camp_gravitatori_selection = RadioGroup(content=Column([
        Radio(value="intensitat_camp_gravitatori", label="Intensitat de camp gravitatori"),
        Radio(value="massa", label="Massa"),
        Radio(value="distancia", label="Distància")]), on_change=camp_gravitatori_radiogroup_changed)

    def button_clicked_camp_gravitatori(e):
        if camp_gravitatori_selection.value == "intensitat_camp_gravitatori":
            intensitat_camp = camp_gravitatori_calcul(massa=float(cg_massa.value), 
                r=float(cg_distancia.value))
            cg_resultat.value = "L'energia mecànica total és de " + str(intensitat_camp) + "m/s^2"
        elif camp_gravitatori_selection.value == "massa":
            massa_final = cg_calcul_massa(cg=float(camp_gravitatori.value), 
                r=float(cg_distancia.value))
            cg_resultat.value = "L'energia mecànica total és de " + str(massa_final) + "kg"
        elif camp_gravitatori_selection.value == "distancia":
            distancia_final = cg_calcul_distancia(cg=float(camp_gravitatori.value), 
                massa=float(cg_massa.value))
            cg_resultat.value = "La distància del cos és de " + str(distancia_final) + "m"
        cg_resultat.visible = True

        page.update()
    cg_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_camp_gravitatori, visible=False)

    camp_gravitatori = TextField(label="Camp gravitatori", visible=False, width=300)
    cg_massa = TextField(label="Massa", visible=False, width=300)
    cg_distancia = TextField(label="Distància", visible=False, width=300)
    cg_resultat = Text(visible=False)

    #VISTA ENERGIA POTENCIAL GRAVITATORIA 

    epg_image = Image(src=f"/imagenes/epg.png")

    def ep_gravitatoria_radiogroup_changed(e):
        if ep_gravitatoria_selection.value == "ep_gravitatoria":
           ep_gravitatoria.visible = False
           epg_massa_1.visible = True
           epg_massa_2.visible = True
           epg_distancia.visible = True
        elif ep_gravitatoria_selection.value == "massa_1":
           ep_gravitatoria.visible = True
           epg_massa_1.visible = False
           epg_massa_2.visible = True
           epg_distancia.visible = True
        elif ep_gravitatoria_selection.value == "massa_2":
           ep_gravitatoria.visible = True
           epg_massa_1.visible = True
           epg_massa_2.visible = False
           epg_distancia.visible = True
        elif ep_gravitatoria_selection.value == "distancia":
           ep_gravitatoria.visible = True
           epg_massa_1.visible = True
           epg_massa_2.visible = True
           epg_distancia.visible = False
        ep_gravitatoria_calcular.visible = True
        page.update()
    
    ep_gravitatoria_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    ep_gravitatoria_selection = RadioGroup(content=Column([
        Radio(value="ep_gravitatoria", label="Energia potencial gravitatoria"),
        Radio(value="massa_1", label="Massa del primer cos"),
        Radio(value="massa_2", label="Massa del segon cos"),
        Radio(value="distancia", label="Distància")]), on_change=ep_gravitatoria_radiogroup_changed)

    def button_clicked_ep_gravitatoria(e):
        if ep_gravitatoria_selection.value == "ep_gravitatoria":
            ep_gravitatoria_total = ep_gravitatoria_calcul(m_1=float(epg_massa_1.value), 
                m_2=float(epg_massa_2.value), r=float(epg_distancia.value))
            epg_resultat.value = "L'energia potencial és de " + str(ep_gravitatoria_total) + " J"
        elif ep_gravitatoria_selection.value == "massa_1":
            epg_massa_c1 = epg_calcular_massa_1(ep=float(ep_gravitatoria.value), 
                r=float(epg_distancia.value), m_2=float(epg_massa_2.value))
            epg_resultat.value = "La massa del primer cos és de " + str(epg_massa_c1) + " kg"
        elif ep_gravitatoria_selection.value == "massa_2":
            epg_massa_c2 = epg_calcular_massa_2(ep=float(ep_gravitatoria.value), 
                r=float(epg_distancia.value), m_1=float(epg_massa_1.value))
            epg_resultat.value = "La massa del segon cos és de " + str(epg_massa_c2) + " kg"
        elif ep_gravitatoria_selection.value == "distancia":
            epg_r = epg_calcular_distancia(ep=float(ep_gravitatoria.value), 
                m_1=float(epg_massa_1.value), m_2=float(epg_massa_2.value))
            epg_resultat.value = "La distancia entre els dos cosos és" + str(epg_r) + " m"
        epg_resultat.visible = True

        page.update()
    ep_gravitatoria_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_ep_gravitatoria, visible=False)


    ep_gravitatoria = TextField(label="Energia potencial gravitatoria", visible=False, width=300)
    epg_massa_1 = TextField(label="Massa del primer cos", visible=False, width=300)
    epg_massa_2 = TextField(label="Massa del segon cos", visible=False, width=300)
    epg_distancia = TextField(label="Distància", visible=False, width=300)
    epg_resultat = Text(visible=False)

    #VISTA LLEI GRAVITACIÓ UNIVERSAL

    gu_image = Image(src=f"/imagenes/gu.png")

    def gravitacio_universal_radiogroup_changed(e):
        if gravitacio_universal_selection.value == "forca_atraccio":
           forca_atraccio.visible = False
           gu_massa_1.visible = True
           gu_massa_2.visible = True
           gu_distancia.visible = True
        elif gravitacio_universal_selection.value == "massa_1":
           forca_atraccio.visible = True
           gu_massa_1.visible = False
           gu_massa_2.visible = True
           gu_distancia.visible = True
        elif gravitacio_universal_selection.value == "massa_2":
           forca_atraccio.visible = True
           gu_massa_1.visible = True
           gu_massa_2.visible = False
           gu_distancia.visible = True
        elif gravitacio_universal_selection.value == "distancia":
           forca_atraccio.visible = True
           gu_massa_1.visible = True
           gu_massa_2.visible = True
           gu_distancia.visible = False
        gravitacio_universal_calcular.visible = True
        page.update()

    gravitacio_universal_text_1 = Text("Que vols calcular?", style=flet.TextThemeStyle.TITLE_MEDIUM, weight=flet.FontWeight.BOLD)
    gravitacio_universal_selection = RadioGroup(content=Column([
        Radio(value="forca_atraccio", label="Força d'atracció"),
        Radio(value="massa_1", label="Massa del primer cos"),
        Radio(value="massa_2", label="Massa del segon cos"),
        Radio(value="distancia", label="Distància")]), on_change=gravitacio_universal_radiogroup_changed)

    def button_clicked_gravitacio_universal(e):
        if gravitacio_universal_selection.value == "forca_atraccio":
            forca_atraccio_total = gu_calcular_forca_atraccio(m_1=float(gu_massa_1.value), 
                m_2=float(gu_massa_2.value), r=float(gu_distancia.value))
            gu_resultat.value = "La força d'atracció entre els planetes és de " + str(forca_atraccio_total) + " N"
        elif gravitacio_universal_selection.value == "massa_1":
            gu_massa_c1 = gu_calcular_massa_1(f=float(forca_atraccio.value), 
                r=float(gu_distancia.value), m_2=float(gu_massa_2.value))
            gu_resultat.value = "La massa del planeta 1 és de " + str(gu_massa_c1) + " kg"
        elif gravitacio_universal_selection.value == "massa_2":
            gu_massa_c2 = gu_calcular_massa_2(f=float(forca_atraccio.value), 
                r=float(gu_distancia.value), m_1=float(gu_massa_1.value))
            gu_resultat.value = "La massa del planeta 2 és de " + str(gu_massa_c2) + " kg"
        elif gravitacio_universal_selection.value == "distancia":
            gu_r = gu_calcular_r(f=float(forca_atraccio.value), 
                m_1=float(gu_massa_1.value), m_2=float(gu_massa_2.value))
            gu_resultat.value = "La distancia entre els dos cosos és " + str(gu_r) + " m"
        gu_resultat.visible = True

        page.update()
    gravitacio_universal_calcular = IconButton(icon=icons.CALCULATE, on_click=button_clicked_gravitacio_universal, visible=False)


    forca_atraccio = TextField(label="Energia potencial gravitatoria", visible=False, width=300)
    gu_massa_1 = TextField(label="Massa del primer cos", visible=False, width=300)
    gu_massa_2 = TextField(label="Massa del segon cos", visible=False, width=300)
    gu_distancia = TextField(label="Distància", visible=False, width=300)
    gu_resultat = Text(visible=False)


    page.on_route_change = route_change
    page.go(page.route)

flet.app(target=main, view=flet.WEB_BROWSER, assets_dir="assets")