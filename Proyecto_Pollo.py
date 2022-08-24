import pygame
from libgrafica import *
import math
from Vistas import *

ANCHO_VENTANA=1400
ALTO_VENTANA=800

def hipotenusa(c1, c2):
    hipo = math.sqrt(pow(c1,2)+pow(c2,2))
    return hipo

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])  
    CENTRO_FIGURA = [900,550]

    r = 0 #ROTACION INICIAL
    trasla = [0,0]
    lis = 1
    #s_aumenta = 6*0.2
    #s_dismin = 4*0.2

    pxl = 20 #PIXELES PARA MODIFICAR EL TAMAÑO

    pygame.display.flip()
   
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            
            vistas_isometricas()

            #----------------------------------------------------- FIGURA --------------------------------------------------
            
            # ============================= PATA 1 =====================================================================================
            #pygame.draw.circle(pantalla,ROJO,CENTRO_FIGURA,4)
            a = [4*pxl,0]       #Rota respecto al centro 30
            b = [1*pxl,0]       #respecto al a 90
            c = [4*pxl,0]       #b 210
            d = [1.66*pxl,0]    #centro 150
            e = [1*pxl,0]       #d 90
            f = [4*pxl,0]       #e 30
            hipo_g = hipotenusa(2,1/3)
            g = [hipo_g*pxl,0]   #c 30+cos(2/hipo_g)
            h = [1*pxl,0]       #g 150
            i = [2*pxl,0]       #h 90
            j = [2*pxl,0]       #g 90
            k = [1*pxl,0]       #g 30
            l = [2*pxl,0]       #k 90

            a = Escala(a,[lis,lis])
            b = Escala(b,[lis,lis])
            c = Escala(c,[lis,lis])
            d = Escala(d,[lis,lis])
            e = Escala(e,[lis,lis])
            f = Escala(f,[lis,lis])
            g = Escala(g,[lis,lis])
            h = Escala(h,[lis,lis])
            i = Escala(i,[lis,lis])
            j = Escala(j,[lis,lis])
            k = Escala(k,[lis,lis])
            l = Escala(l,[lis,lis])


            
            # ============================================================
            a_r =Rotacion_h(a,r+30)
            a_rc = Pantalla_Cartesiano(a_r, CENTRO_FIGURA)

            b_r = Rotacion_h(b,r+90)
            b_rc = Pantalla_Cartesiano(b_r, a_rc)

            c_r = Rotacion_h(c,r+210)
            c_rc = Pantalla_Cartesiano(c_r, b_rc)
            # ====================================================================
            d_r =Rotacion_h(d,r+150)
            d_rc = Pantalla_Cartesiano(d_r, CENTRO_FIGURA)

            e_r = Rotacion_h(e,r+90)
            e_rc = Pantalla_Cartesiano(e_r, d_rc)
            # ====================================================================
            f_r = Rotacion_h(f,r+30)
            f_rc = Pantalla_Cartesiano(f_r, e_rc)
            # ====================================================================
            g_r =Rotacion_h(g,r+30+math.cos(2/hipo_g))
            g_rc = Pantalla_Cartesiano(g_r, c_rc)

            h_r = Rotacion_h(h,r+150)
            h_rc = Pantalla_Cartesiano(h_r, g_rc)

            i_r = Rotacion_h(i,r+90)
            i_rc = Pantalla_Cartesiano(i_r, h_rc)

            j_r = Rotacion_h(j,r+90)
            j_rc = Pantalla_Cartesiano(j_r, g_rc)
            
            # ====================================================================
            k_r = Rotacion_h(k,r+30)
            k_rc = Pantalla_Cartesiano(k_r, g_rc)

            l_r = Rotacion_h(l,r+90)
            l_rc = Pantalla_Cartesiano(l_r, k_rc)

            # ==============================PATA 2========================================================================================
            #El punto de referencia es d
            CENTRO_FIGURA_AUX = [0.34*pxl, 0]       #d 150
            za = [4*pxl,0]       #centro_figura_aux 30
            zb = [1*pxl,0]       #respecto al a 90
            zc = [4*pxl,0]       #b 210
            zd = [1.66*pxl,0]    #centro 150
            ze = [1*pxl,0]       #d 90
            zf = [4*pxl,0]       #e 30
            zg = [hipo_g*pxl,0]   #c 30+cos(2/hipo_g)
            zh = [1*pxl,0]       #g 150
            zi = [2*pxl,0]       #h 90
            zj = [2*pxl,0]       #g 90
            zk = [1*pxl,0]       #g 30
            zl = [2*pxl,0]       #k 90

            za = Escala(za,[lis,lis])
            zb = Escala(zb,[lis,lis])
            zc = Escala(zc,[lis,lis])
            zd = Escala(zd,[lis,lis])
            ze = Escala(ze,[lis,lis])
            zf = Escala(zf,[lis,lis])
            zg = Escala(zg,[lis,lis])
            zh = Escala(zh,[lis,lis])
            zi = Escala(zi,[lis,lis])
            zj = Escala(zj,[lis,lis])
            zk = Escala(zk,[lis,lis])
            zl = Escala(zl,[lis,lis])
            
            # ============================================================
            CENTRO_FIGURA_AUX_r =Rotacion_h(CENTRO_FIGURA_AUX,r+150)
            CENTRO_FIGURA_AUX_rc = Pantalla_Cartesiano(CENTRO_FIGURA_AUX_r, d_rc)

            za_r =Rotacion_h(za,r+30)
            za_rc = Pantalla_Cartesiano(za_r, CENTRO_FIGURA_AUX_rc)

            zb_r = Rotacion_h(zb,r+90)
            zb_rc = Pantalla_Cartesiano(zb_r, za_rc)

            zc_r = Rotacion_h(zc,r+210)
            zc_rc = Pantalla_Cartesiano(zc_r, zb_rc)
            # ====================================================================
            zd_r =Rotacion_h(zd,r+150)
            zd_rc = Pantalla_Cartesiano(zd_r, d_rc)

            ze_r = Rotacion_h(ze,r+90)
            ze_rc = Pantalla_Cartesiano(ze_r, zd_rc)
            # ====================================================================
            zf_r = Rotacion_h(zf,r+30)
            zf_rc = Pantalla_Cartesiano(zf_r, ze_rc)
            # ====================================================================
            zg_r =Rotacion_h(zg,r+30+math.cos(2/hipo_g))
            zg_rc = Pantalla_Cartesiano(zg_r, zc_rc)

            zh_r = Rotacion_h(zh,r+150)
            zh_rc = Pantalla_Cartesiano(zh_r, zg_rc)

            zi_r = Rotacion_h(zi,r+90)
            zi_rc = Pantalla_Cartesiano(zi_r, zh_rc)

            zj_r = Rotacion_h(zj,r+90)
            zj_rc = Pantalla_Cartesiano(zj_r, zg_rc)
            
            # ====================================================================
            zk_r = Rotacion_h(zk,r+30)
            zk_rc = Pantalla_Cartesiano(zk_r, zg_rc)

            zl_r = Rotacion_h(zl,r+90)
            zl_rc = Pantalla_Cartesiano(zl_r, zk_rc)

            #IMPRIMIMOS LA PATA 2 ANTES QUE LA 1
            polig_1_pata_2 = [CENTRO_FIGURA_AUX_rc, za_rc, zb_rc, zc_rc]
            pygame.draw.polygon(pantalla, NARANJA, polig_1_pata_2)

            polig_2_pata_2 = [CENTRO_FIGURA_AUX_rc, zd_rc, ze_rc, zc_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO, polig_2_pata_2)

            polig_3_pata_2 = [zc_rc, ze_rc, zf_rc, zb_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO_CLARO, polig_3_pata_2)
        
            polig_4_pata_2 = [zg_rc, zh_rc, zi_rc, zj_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO, polig_4_pata_2)
            
            polig_5_pata_2 = [zg_rc, zj_rc, zl_rc, zk_rc]
            pygame.draw.polygon(pantalla, NARANJA, polig_5_pata_2)

            #IMPRIMIMOS LA PATA 1 DESPUES DE LA 2, PORQUE LA 2 ESTA DEBAJO
            polig_1_pata_1 = [CENTRO_FIGURA, a_rc, b_rc, c_rc]
            pygame.draw.polygon(pantalla, NARANJA, polig_1_pata_1)

            polig_2_pata_1 = [CENTRO_FIGURA, d_rc, e_rc, c_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO, polig_2_pata_1)

            polig_3_pata_1 = [c_rc, e_rc, f_rc, b_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO_CLARO, polig_3_pata_1)

            polig_4_pata_1 = [g_rc, h_rc, i_rc, j_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO, polig_4_pata_1)

            polig_5_pata_1 = [g_rc, j_rc, l_rc, k_rc]
            pygame.draw.polygon(pantalla, NARANJA, polig_5_pata_1)


            # ============================= CUERPO ===========================================================================
            #El punto de referencia sera j
            n = [3*pxl,0]       #j 210
            m = [5*pxl,0]       #n 150
            o = [9*pxl,0]       #m 90
            p = [5*pxl,0]       #o 330
            q = [5*pxl,0]       #o 30
            rr = [5*pxl,0]       #q 330
            s = [5*pxl,0]       #r 270
            t = [3*pxl,0]       #s 30
            u = [4*pxl,0]       #t 270
            v = [5*pxl,0]       #t 150

            n = Escala(n,[lis,lis])
            m = Escala(m,[lis,lis])
            o = Escala(o,[lis,lis])
            p = Escala(p,[lis,lis])
            q = Escala(q,[lis,lis])
            rr = Escala(rr,[lis,lis])
            s = Escala(s,[lis,lis])
            t = Escala(t,[lis,lis])
            u = Escala(u,[lis,lis])
            v = Escala(v,[lis,lis])

            n_r =Rotacion_h(n, r+210)
            n_rc = Pantalla_Cartesiano(n_r, j_rc)

            m_r =Rotacion_h(m,r+150)
            m_rc = Pantalla_Cartesiano(m_r, n_rc)

            o_r =Rotacion_h(o,r+90)
            o_rc = Pantalla_Cartesiano(o_r, m_rc)

            p_r =Rotacion_h(p,r+330)
            p_rc = Pantalla_Cartesiano(p_r, o_rc)

            q_r =Rotacion_h(q,r+30)
            q_rc = Pantalla_Cartesiano(q_r, o_rc)

            rr_r =Rotacion_h(rr,r+330)
            rr_rc = Pantalla_Cartesiano(rr_r, q_rc)

            s_r =Rotacion_h(s,r+270)
            s_rc = Pantalla_Cartesiano(s_r, rr_rc)

            t_r =Rotacion_h(t,r+30)
            t_rc = Pantalla_Cartesiano(t_r, s_rc)

            u_r =Rotacion_h(u,r+270)
            u_rc = Pantalla_Cartesiano(u_r, t_rc)

            v_r =Rotacion_h(v,r+150)
            v_rc = Pantalla_Cartesiano(v_r, t_rc)

            #IMPRIMIMOS EL CUERPO DEL POLLO
            polig_cuerpo_1 = [t_rc, v_rc, s_rc]
            pygame.draw.polygon(pantalla, BLANCO, polig_cuerpo_1)

            polig_cuerpo_2 = [m_rc, n_rc, p_rc, o_rc]
            pygame.draw.polygon(pantalla, BLANCO, polig_cuerpo_2)

            polig_cuerpo_3 = [o_rc, p_rc, rr_rc, q_rc]
            pygame.draw.polygon(pantalla, GRIS, polig_cuerpo_3)

            polig_cuerpo_4 = [p_rc, rr_rc, s_rc, t_rc, u_rc, n_rc]
            pygame.draw.polygon(pantalla, GRIS_CLARO, polig_cuerpo_4)


            # ============================= ALA ===========================================================================
            punto_auxiliar_ala = [1*pxl, 0]      #s 270
            ac = [1*pxl, 0]     #punto_auxiliar 30
            x = [1*pxl, 0]      #ac 330
            y = [5*pxl, 0]      #x 210
            ab = [1*pxl, 0]     #y 150
            aa = [2*pxl, 0]     #ab 270
            z = [1*pxl, 0]      #aa 330
            w = [5*pxl, 0]      #z 30

            punto_auxiliar_ala = Escala(punto_auxiliar_ala,[lis,lis])
            ac = Escala(ac,[lis,lis])
            x = Escala(x,[lis,lis])
            y = Escala(y,[lis,lis])
            ab = Escala(ab,[lis,lis])
            aa = Escala(aa,[lis,lis])
            z = Escala(z,[lis,lis])
            w = Escala(w,[lis,lis])

            punto_auxiliar_r = Rotacion_h(punto_auxiliar_ala, r+270)
            punto_auxiliar_rc = Pantalla_Cartesiano(punto_auxiliar_r, s_rc)

            ac_r =Rotacion_h(ac,r+30)
            ac_rc = Pantalla_Cartesiano(ac_r, punto_auxiliar_rc)

            x_r =Rotacion_h(x,r+330)
            x_rc = Pantalla_Cartesiano(x_r, ac_rc)

            y_r =Rotacion_h(y,r+210)
            y_rc = Pantalla_Cartesiano(y_r, x_rc)

            ab_r =Rotacion_h(ab,r+150)
            ab_rc = Pantalla_Cartesiano(ab_r, y_rc)

            aa_r =Rotacion_h(aa,r+270)
            aa_rc = Pantalla_Cartesiano(aa_r, ab_rc)

            z_r =Rotacion_h(z,r+330)
            z_rc = Pantalla_Cartesiano(z_r, aa_rc)

            w_r =Rotacion_h(w,r+30)
            w_rc = Pantalla_Cartesiano(w_r, z_rc)

            #IMPRIMIMOS EL ALA DEL POLLO
            polig_ala_1 = [ac_rc, x_rc, y_rc, ab_rc]
            pygame.draw.polygon(pantalla, BLANCO, polig_ala_1)

            polig_ala_2 = [ab_rc, y_rc, z_rc, aa_rc]
            pygame.draw.polygon(pantalla, BLANCO, polig_ala_2)

            polig_ala_3 = [z_rc, y_rc, x_rc, w_rc]
            pygame.draw.polygon(pantalla, GRIS_CLARO, polig_ala_3)


            # ============================= BARBILLA ===========================================================================
            barbilla_aux = [2*pxl, 0]       #p 150
            ad = [4*pxl, 0]     #barbilla_aux 270
            ae = [2*pxl, 0]     #ad 270
            af = [1*pxl, 0]     #ae 210
            ag = [1*pxl, 0]     #af 150
            ah = [2*pxl, 0]     #ag 90
            ai = [1*pxl, 0]     #ah 330

            barbilla_aux = Escala(barbilla_aux,[lis,lis])
            ad = Escala(ad,[lis,lis])
            ae = Escala(ae,[lis,lis])
            af = Escala(af,[lis,lis])
            ag = Escala(ag,[lis,lis])
            ah = Escala(ah,[lis,lis])
            ai = Escala(ai,[lis,lis])
            

            barbilla_aux_r =Rotacion_h(barbilla_aux,r+150)
            barbilla_aux_rc = Pantalla_Cartesiano(barbilla_aux_r, p_rc)

            ad_r =Rotacion_h(ad,r+270)
            ad_rc = Pantalla_Cartesiano(ad_r, barbilla_aux_rc)

            ae_r =Rotacion_h(ae,r+270)
            ae_rc = Pantalla_Cartesiano(ae_r, ad_rc)

            af_r =Rotacion_h(af,r+210)
            af_rc = Pantalla_Cartesiano(af_r, ae_rc)

            ag_r =Rotacion_h(ag,r+150)
            ag_rc = Pantalla_Cartesiano(ag_r, af_rc)

            ah_r =Rotacion_h(ah,r+90)
            ah_rc = Pantalla_Cartesiano(ah_r, ag_rc)

            ai_r =Rotacion_h(ai,r+330)
            ai_rc = Pantalla_Cartesiano(ai_r, ah_rc)

            #IMPRIMIMOS LA BARBILLA DEL POLLO
            polig_barbilla_1 = [ad_rc, ae_rc, af_rc, ai_rc]
            pygame.draw.polygon(pantalla, ROSA, polig_barbilla_1)

            polig_barbilla_2 = [ai_rc, af_rc, ag_rc, ah_rc]
            pygame.draw.polygon(pantalla, ROSA_CLARO_CLARO, polig_barbilla_2)

            # ============================= PICO ===========================================================================
            #El punto de referencia sera ad
            aj = [2*pxl, 0]     #ad 90
            ak = [1*pxl, 0]     #aj 150
            al = [2*pxl, 0]     #ak 210
            am = [1*pxl, 0]     #al 330
            an = [2*pxl, 0]     #am 270
            ao = [1*pxl, 0]     #an 150

            aj = Escala(aj,[lis,lis])
            ak = Escala(ak,[lis,lis])
            al = Escala(al,[lis,lis])
            am = Escala(am,[lis,lis])
            an = Escala(an,[lis,lis])
            ao = Escala(ao,[lis,lis])

            aj_r =Rotacion_h(aj,r+90)
            aj_rc = Pantalla_Cartesiano(aj_r, ad_rc)

            ak_r =Rotacion_h(ak,r+150)
            ak_rc = Pantalla_Cartesiano(ak_r, aj_rc)

            al_r =Rotacion_h(al,r+210)
            al_rc = Pantalla_Cartesiano(al_r, ak_rc)

            am_r =Rotacion_h(am,r+330)
            am_rc = Pantalla_Cartesiano(am_r, al_rc)

            an_r =Rotacion_h(an,r+270)
            an_rc = Pantalla_Cartesiano(an_r, am_rc)

            ao_r =Rotacion_h(ao,r+150)
            ao_rc = Pantalla_Cartesiano(ao_r, an_rc)

            #IMPRIMIMOS EL PICO DEL POLLO
            polig_pico_1 = [aj_rc, ak_rc, al_rc, am_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO, polig_pico_1)

            polig_pico_2 = [aj_rc, ad_rc, an_rc, am_rc]
            pygame.draw.polygon(pantalla, NARANJA, polig_pico_2)

            polig_pico_3 = [am_rc, an_rc, ao_rc, al_rc]
            pygame.draw.polygon(pantalla, NARANJA_CLARO_CLARO, polig_pico_3)

            # ============================= OJO 1 ===========================================================================
            #Punto de referencia ak
            ap = [1*pxl, 0]     #ak 150
            aq = [1*pxl, 0]     #ap 90
            ar = [1*pxl, 0]     #aq 330

            ap = Escala(ap,[lis,lis])
            aq = Escala(aq,[lis,lis])
            ar = Escala(ar,[lis,lis])

            ap_r =Rotacion_h(ap,r+150)
            ap_rc = Pantalla_Cartesiano(ap_r, ak_rc)

            aq_r =Rotacion_h(aq,r+90)
            aq_rc = Pantalla_Cartesiano(aq_r, ap_rc)

            ar_r =Rotacion_h(ar,r+330)
            ar_rc = Pantalla_Cartesiano(ar_r, aq_rc)

            #IMPRIMIMOS EL OJO 1 DEL POLLO
            polig_ojo_1 = [ak_rc, ap_rc, aq_rc, ar_rc]
            pygame.draw.polygon(pantalla, NEGRO, polig_ojo_1)

            # ============================= OJO 2 ===========================================================================
            #Punto de referencia aj
            ass = [1*pxl, 0]     #aj 330
            at = [1*pxl, 0]     #ass 90
            au = [1*pxl, 0]     #at 150

            ass = Escala(ass,[lis,lis])
            at = Escala(at,[lis,lis])
            au = Escala(au,[lis,lis])

            ass_r =Rotacion_h(ass,r+330)
            ass_rc = Pantalla_Cartesiano(ass_r, aj_rc)

            at_r =Rotacion_h(at,r+90)
            at_rc = Pantalla_Cartesiano(at_r, ass_rc)

            au_r =Rotacion_h(au,r+150)
            au_rc = Pantalla_Cartesiano(au_r, at_rc)

            #IMPRIMIMOS EL OJO 2 DEL POLLO
            polig_ojo_2 = [aj_rc, ass_rc, at_rc, au_rc]
            pygame.draw.polygon(pantalla, NEGRO, polig_ojo_2)

            # ============================= CRESTA ===========================================================================
            cresta_aux = barbilla_aux
            av = [1*pxl, 0]     #cresta_aux 30
            aw = [1*pxl, 0]     #av 150
            ay = [1*pxl, 0]     #aw 90
            ax = [1*pxl, 0]     #ay 330
            az = [3*pxl, 0]     #ay 30
            ba = [1*pxl, 0]     #az 330
            bb = [1*pxl, 0]     #ba 270

            #Cresta_aux ya esta escalada
            av = Escala(av,[lis,lis])
            aw = Escala(aw,[lis,lis])
            ay = Escala(ay,[lis,lis])
            ax = Escala(ax,[lis,lis])
            az = Escala(az,[lis,lis])
            ba = Escala(ba,[lis,lis])
            bb = Escala(bb,[lis,lis])

            cresta_aux_r =Rotacion_h(cresta_aux,r+150)
            cresta_aux_rc = Pantalla_Cartesiano(cresta_aux_r, p_rc)

            av_r =Rotacion_h(av,r+30)
            av_rc = Pantalla_Cartesiano(av_r, cresta_aux_rc)

            aw_r =Rotacion_h(aw,r+150)
            aw_rc = Pantalla_Cartesiano(aw_r, av_rc)

            ay_r =Rotacion_h(ay,r+90)
            ay_rc = Pantalla_Cartesiano(ay_r, aw_rc)

            ax_r =Rotacion_h(ax,r+330)
            ax_rc = Pantalla_Cartesiano(ax_r, ay_rc)

            az_r =Rotacion_h(az,r+30)
            az_rc = Pantalla_Cartesiano(az_r, ay_rc)

            ba_r =Rotacion_h(ba,r+330)
            ba_rc = Pantalla_Cartesiano(ba_r, az_rc)

            bb_r =Rotacion_h(bb,r+270)
            bb_rc = Pantalla_Cartesiano(bb_r, ba_rc)

            #IMPRIMIMOS LA CRESTA DEL POLLO
            polig_cresta_1 = [av_rc, aw_rc, ay_rc, ax_rc]
            pygame.draw.polygon(pantalla, ROSA_CLARO_CLARO, polig_cresta_1)

            polig_cresta_2 = [ay_rc, ax_rc, ba_rc, az_rc]
            pygame.draw.polygon(pantalla, ROSA_CLARO, polig_cresta_2)

            polig_cresta_3 = [ba_rc, ax_rc, av_rc, bb_rc]
            pygame.draw.polygon(pantalla, ROSA, polig_cresta_3)

            #Para hacer la rotacion
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #Antihorario
                    r += 5
                if event.key == pygame.K_DOWN: #Horario
                    r -= 5
                if event.key == pygame.K_LEFT and CENTRO_FIGURA[0] > 700:
                    trasla = [-10,0]
                    CENTRO_FIGURA = Traslacion(CENTRO_FIGURA,trasla)
                    print(CENTRO_FIGURA)
                if event.key == pygame.K_RIGHT and CENTRO_FIGURA[0] < 1200:
                    trasla = [10,0]
                    print(CENTRO_FIGURA)
                    CENTRO_FIGURA = Traslacion(CENTRO_FIGURA,trasla)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and lis<4:
                    #AUMENTAR
                    lis += 0.1
                if event.button == 5 and lis>0.2:
                    #DISMINUIR
                    lis -= 0.1
                    
        pygame.display.flip()
        
    pygame.quit()
        
