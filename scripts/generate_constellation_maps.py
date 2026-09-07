from math import sin, cos, tan, asin, atan2, radians, degrees, pi
from pathlib import Path

LAT = radians(50.0)
OUT = Path('/home/tofdan/Projets_Dev/wiki-oca/docs/assets/formation-guide-astro/constellations')

stars = {
    'grande-ourse': {
        'title': 'Grande Ourse — Ursa Major',
        'stars': [
            ('Dubhe', 'α UMa', 11+3/60+43/3600, 61.75, 1.79),
            ('Merak', 'β UMa', 11+1/60+50/3600, 56.38, 2.37),
            ('Phecda', 'γ UMa', 11+53/60+49/3600, 53.69, 2.44),
            ('Megrez', 'δ UMa', 12+15/60+25/3600, 57.03, 3.31),
            ('Alioth', 'ε UMa', 12+54/60+1/3600, 55.96, 1.77),
            ('Mizar', 'ζ UMa', 13+23/60+56/3600, 54.93, 2.27),
            ('Alkaid', 'η UMa', 13+47/60+32/3600, 49.31, 1.86),
            ('Alcor', '80 UMa', 13+25/60+14/3600, 54.99, 4.00),
            ('Psi UMa', 'ψ UMa', 11+9/60, 44.50, 3.01),
            ('Theta UMa', 'θ UMa', 9+32/60, 51.60, 3.17),
            ('Iota UMa', 'ι UMa', 8+59/60, 48.04, 3.14),
        ],
        # Grand Chariot + silhouette pédagogique de l’Ourse. Mizar et Alcor sont
        # deux étoiles distinctes ; Alcor n’est pas reliée par un segment.
        'lines': [(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,6),
                  (2,7),(7,8),(8,9),(9,0)],
    },
    'hercule': {
        'title': 'Hercule — Hercules',
        'stars': [
            ('Kornephoros', 'β Her', 16+30/60+13/3600, 21.49, 2.80),
            ('Ras Algethi', 'α Her', 17+14/60+39/3600, 14.39, 2.78),
            ('Pi Her', 'π Her', 17+15/60+2/3600, 36.81, 3.16),
            ('Eta Her', 'η Her', 16+42/60+53/3600, 38.92, 3.49),
            ('Zeta Her', 'ζ Her', 16+41/60+17/3600, 31.60, 2.81),
            ('Epsilon Her', 'ε Her', 17+0/60+18/3600, 30.93, 3.92),
            ('Delta Her', 'δ Her', 17+15/60+2/3600, 24.84, 3.12),
            ('Gamma Her', 'γ Her', 16+21/60+55/3600, 19.15, 3.74),
            ('Theta Her', 'θ Her', 17+56/60+16/3600, 37.25, 3.86),
            ('Iota Her', 'ι Her', 17+39/60+28/3600, 46.01, 3.80),
            ('Kappa Her', 'κ Her', 16+8/60+4/3600, 17.05, 5.00),
            ('Lambda Her', 'λ Her', 17+30/60+44/3600, 26.11, 4.40),
            ('Mu Her', 'μ Her', 17+46/60+28/3600, 27.72, 3.42),
            ('Rho Her', 'ρ Her', 17+23/60+41/3600, 37.15, 4.16),
        ],
        # Keystone: Pi-Eta-Zeta-Epsilon. Les autres segments complètent
        # la figure pédagogique d'Hercule sans prétendre à une norme unique.
        'lines': [(2,3),(3,4),(4,5),(5,2),
                  (3,8),(8,9),(9,10),       # tête / jambe nord
                  (2,13),(13,0),            # bras vers Kornephoros
                  (4,6),(6,1),(1,11),(11,12)],
    },
    'cephee': {
        'title': 'Céphée — Cepheus',
        'stars': [
            ('Alderamin', 'α Cep', 21+18/60+34/3600, 62.59, 2.44),
            ('Alfirk', 'β Cep', 21+28/60+39/3600, 70.56, 3.23),
            ('Errai', 'γ Cep', 23+39/60+20/3600, 77.63, 3.21),
            ('Delta Cephei', 'δ Cep', 22+29/60+10/3600, 58.42, 3.95),
            ('Zeta Cephei', 'ζ Cep', 22+10/60+51/3600, 58.20, 3.35),
            ('Iota Cephei', 'ι Cep', 22+50/60, 66.20, 3.52),
            ('Mu Cephei', 'μ Cep', 21+43/60+30/3600, 58.78, 4.10),
        ],
        # Maison classique : Errai-Alfirk-Iota-Alderamin-Delta-Errai.
        # Zeta et Mu sont conservées comme étoiles remarquables, non reliées.
        'lines': [(2,1),(1,5),(5,0),(0,3),(3,2)],
    },
}

def jd(year, month, day, hour):
    if month <= 2:
        year -= 1; month += 12
    a = year // 100
    b = 2 - a + a // 4
    return int(365.25*(year+4716)) + int(30.6001*(month+1)) + day + b - 1524.5 + hour/24

def lst_hours(year, month, day, utc_hour, lon=4.5):
    j = jd(year, month, day, utc_hour)
    d = j - 2451545.0
    gmst = (18.697374558 + 24.06570982441908*d) % 24
    return (gmst + lon/15) % 24

def altaz(ra_h, dec_deg, lst_h):
    H = radians((lst_h - ra_h)*15)
    dec = radians(dec_deg)
    alt = asin(sin(LAT)*sin(dec) + cos(LAT)*cos(dec)*cos(H))
    az = atan2(-sin(H)*cos(dec), sin(dec)*cos(LAT)-cos(dec)*sin(LAT)*cos(H))
    return degrees(alt), (degrees(az)+360)%360

def star_size(mag):
    return max(3.0, 8.0 - 1.15*mag)

def panel(data, x0, label, year, month, day, utc_hour):
    w, h = 700, 510
    cx, cy, R = x0+350, 305, 205
    lst = lst_hours(year, month, day, utc_hour)
    coords=[]
    for name, greek, ra, dec, mag in data['stars']:
        alt, az = altaz(ra, dec, lst)
        if alt >= 0:
            rr = R*(90-alt)/90
            x = cx + rr*sin(radians(az)); y = cy - rr*cos(radians(az))
            coords.append((x,y,alt,az,name,greek,mag))
        else:
            coords.append((None,None,alt,az,name,greek,mag))
    s=[]
    s.append(f'<g><rect x="{x0}" y="0" width="{w}" height="510" rx="12" fill="#071326" stroke="#7187a8"/>')
    s.append(f'<text x="{x0+350}" y="30" text-anchor="middle" fill="#ffffff" font-size="19" font-family="sans-serif" font-weight="bold">{label}</text>')
    s.append(f'<text x="{x0+350}" y="52" text-anchor="middle" fill="#b9c9df" font-size="13" font-family="sans-serif">latitude 50° N — Nord en haut — Est à droite — LST {lst:.2f} h</text>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#0b1d37" stroke="#8297b6" stroke-width="2"/>')
    for alt in (30,60):
        r=R*(90-alt)/90
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="#314b70" stroke-dasharray="4 5"/>')
        s.append(f'<text x="{cx+5}" y="{cy-r+14:.1f}" fill="#839bbd" font-size="11" font-family="sans-serif">{alt}°</text>')
    for az, txt in [(0,'N'),(90,'E'),(180,'S'),(270,'O')]:
        x=cx+(R+18)*sin(radians(az)); y=cy-(R+18)*cos(radians(az))+5
        s.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" fill="#ffffff" font-size="15" font-family="sans-serif" font-weight="bold">{txt}</text>')
    for i,j in data['lines']:
        a,b=coords[i],coords[j]
        if a[0] is not None and b[0] is not None:
            s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#91a8c8" stroke-width="1.5"/>')
    for x,y,alt,az,name,greek,mag in coords:
        if x is None: continue
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{star_size(mag):.1f}" fill="#ffe28a" stroke="#fff8d0"/>')
        dx,dy=10,-8
        if x > cx+130: dx=-115
        s.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" fill="#ffffff" font-size="11" font-family="sans-serif">{name} ({mag:g})</text>')
    s.append(f'<text x="{x0+350}" y="493" text-anchor="middle" fill="#9eb1cb" font-size="11" font-family="sans-serif">Cercle extérieur = horizon ; centre = zénith ; étoiles sous l’horizon non dessinées</text></g>')
    return ''.join(s)

def focused_map(data, label, year, month, day, utc_hour):
    """Agrandissement pédagogique de la figure, en conservant la géométrie locale."""
    lst = lst_hours(year, month, day, utc_hour)
    raw=[]
    for name, greek, ra, dec, mag in data['stars']:
        alt, az = altaz(ra, dec, lst)
        if alt >= 0:
            raw.append((az, alt, name, greek, mag))
    # Coordonnées locales : azimut horizontal, altitude verticale.
    # On agrandit uniquement l'emprise de la constellation visible.
    xs=[sin(radians(a))*(90-al)/90 for a,al,*_ in raw]
    ys=[-cos(radians(a))*(90-al)/90 for a,al,*_ in raw]
    xmin,xmax=min(xs),max(xs); ymin,ymax=min(ys),max(ys)
    margin=0.16
    xmin-=margin; xmax+=margin; ymin-=margin; ymax+=margin
    W,H=900,620
    left,top,right,bottom=90,105,810,535
    def xy(x,y):
        return (left+(x-xmin)/(xmax-xmin)*(right-left),
                top+(y-ymin)/(ymax-ymin)*(bottom-top))
    coords=[]
    visible_by_name={name:(az,alt,mag) for az,alt,name,greek,mag in raw}
    for name,greek,ra,dec,mag in data['stars']:
        if name in visible_by_name:
            az,alt,_=visible_by_name[name]
            x,y=xy(sin(radians(az))*(90-alt)/90,-cos(radians(az))*(90-alt)/90)
            coords.append((x,y,alt,az,name,greek,mag))
        else:
            coords.append((None,None,-1,0,name,greek,mag))
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{data["title"]}, dessin pédagogique orienté pour le 7 septembre 2026 à 22 heures">']
    out.append('<rect width="900" height="620" fill="#050d1b"/>')
    out.append(f'<text x="450" y="38" text-anchor="middle" fill="#ffffff" font-size="26" font-family="sans-serif" font-weight="bold">{data["title"]}</text>')
    out.append(f'<text x="450" y="67" text-anchor="middle" fill="#bdd0e8" font-size="16" font-family="sans-serif">Dessin à reproduire — Belgique, 7 septembre 2026, 22 h CEST — latitude 50° N</text>')
    out.append(f'<rect x="{left}" y="{top}" width="{right-left}" height="{bottom-top}" rx="18" fill="#0a1c34" stroke="#6682a8" stroke-width="2"/>')
    # Repère local discret : N en haut, E à droite, O à gauche.
    out.append(f'<text x="450" y="92" text-anchor="middle" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold">N</text>')
    out.append(f'<text x="{right+24}" y="320" text-anchor="middle" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold">E</text>')
    out.append(f'<text x="{left-24}" y="320" text-anchor="middle" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold">O</text>')
    for i,j in data['lines']:
        a,b=coords[i],coords[j]
        if a[0] is not None and b[0] is not None:
            out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#b6c9e4" stroke-width="3" stroke-linecap="round"/>')
    for x,y,alt,az,name,greek,mag in coords:
        if x is None: continue
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{max(5,10-1.1*mag):.1f}" fill="#ffdf72" stroke="#fff9d5" stroke-width="1.5"/>')
        # Les noms sont placés hors de la ligne autant que possible.
        dx,dy=12,-10
        if x>700: dx=-145
        if y<145: dy=20
        out.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" fill="#ffffff" font-size="15" font-family="sans-serif">{name} — mag. {mag:g}</text>')
    out.append('<text x="450" y="580" text-anchor="middle" fill="#a9bdd8" font-size="14" font-family="sans-serif">Agrandissement pédagogique : la forme est conservée, mais la carte n’est pas à l’échelle.</text>')
    out.append('</svg>')
    return ''.join(out)

def clean_hercules_map():
    """Dessin classique simplifié d'Hercule, indépendant du lieu et de la date."""
    # Figure classique inspirée de la carte IAU/Sky & Telescope reprise par
    # Wikipedia : le Keystone forme le torse, avec les extensions du héros.
    pos = {
        'Eta Her': (330, 235), 'Pi Her': (565, 235),
        'Zeta Her': (365, 405), 'Epsilon Her': (535, 405),
        'Kornephoros': (690, 275), 'Ras Algethi': (735, 475),
        'Gamma Her': (785, 185), 'Delta Her': (635, 500),
        'Theta Her': (285, 120), 'Iota Her': (205, 75),
        'Kappa Her': (865, 170), 'Lambda Her': (685, 390),
        'Mu Her': (700, 550), 'Rho Her': (520, 120),
    }
    mags = {name: mag for name, greek, ra, dec, mag in stars['hercule']['stars']}
    greek = {name: greek for name, greek, ra, dec, mag in stars['hercule']['stars']}
    # Keystone puis extensions classiques ; les segments restent lisibles.
    lines = [
        ('Eta Her','Pi Her'), ('Pi Her','Epsilon Her'),
        ('Epsilon Her','Zeta Her'), ('Zeta Her','Eta Her'),
        ('Pi Her','Rho Her'), ('Rho Her','Theta Her'), ('Theta Her','Iota Her'),
        ('Pi Her','Kornephoros'), ('Kornephoros','Gamma Her'), ('Gamma Her','Kappa Her'),
        ('Eta Her','Theta Her'), ('Zeta Her','Delta Her'), ('Delta Her','Ras Algethi'),
        ('Epsilon Her','Lambda Her'), ('Lambda Her','Mu Her'),
    ]
    W,H=980,680
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Hercule, dessin pédagogique de la constellation">']
    out.append('<rect width="980" height="680" fill="#050d1b"/>')
    out.append('<text x="490" y="38" text-anchor="middle" fill="#ffffff" font-size="28" font-family="sans-serif" font-weight="bold">Hercule — dessin pédagogique</text>')
    out.append('<text x="490" y="68" text-anchor="middle" fill="#bdd0e8" font-size="16" font-family="sans-serif">Figure classique — représentation pédagogique, indépendante de la date et du lieu</text>')
    out.append('<rect x="90" y="95" width="800" height="510" rx="20" fill="#0a1c34" stroke="#6682a8" stroke-width="2"/>')
    out.append('<text x="490" y="120" text-anchor="middle" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold">N</text>')
    out.append('<text x="920" y="355" text-anchor="middle" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold">E</text>')
    out.append('<text x="60" y="355" text-anchor="middle" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold">O</text>')
    out.append('<text x="450" y="155" text-anchor="middle" fill="#93b4da" font-size="15" font-family="sans-serif">KEYSTONE — torse d’Hercule</text>')
    for a,b in lines:
        x1,y1=pos[a]; x2,y2=pos[b]
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#b6c9e4" stroke-width="3" stroke-linecap="round"/>')
    for name,(x,y) in pos.items():
        mag=mags[name]
        out.append(f'<circle cx="{x}" cy="{y}" r="{max(5,10-1.1*mag):.1f}" fill="#ffdf72" stroke="#fff9d5" stroke-width="1.5"/>')
        dx,dy=12,-10
        if x>760: dx=-150
        if name in ('Eta Her','Pi Her','Theta Her','Iota Her'): dy=20
        out.append(f'<text x="{x+dx}" y="{y+dy}" fill="#ffffff" font-size="15" font-family="sans-serif">{name} — mag. {mag:g}</text>')
    out.append('<text x="490" y="642" text-anchor="middle" fill="#a9bdd8" font-size="14" font-family="sans-serif">Figure classique agrandie : la forme est pédagogique et non à l’échelle.</text>')
    out.append('</svg>')
    return ''.join(out)

for key,data in stars.items():
    focused = focused_map(data,'',2026,9,7,20)
    (OUT/f'{key}-pedagogique-22h.svg').write_text(focused, encoding='utf-8')
    if key == 'hercule':
        # Le dessin classique ne doit pas être remplacé par la carte locale agrandie.
        (OUT/'hercule-pedagogique-22h.svg').write_text(clean_hercules_map(), encoding='utf-8')
    svg22 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 510" role="img" aria-label="{data['title']} le 7 septembre 2026 à 22 heures en Belgique">
<rect width="700" height="510" fill="#030914"/>
{panel(data,0,'7 septembre 2026 — 22 h CEST',2026,9,7,20)}
</svg>'''
    (OUT/f'{key}-oriente-22h.svg').write_text(svg22, encoding='utf-8')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1450 510" role="img" aria-label="{data['title']} le 7 septembre 2026 à 22 heures et le 8 septembre à 5 heures en Belgique">
<rect width="1450" height="510" fill="#030914"/>
<text x="725" y="18" text-anchor="middle" fill="#dce9ff" font-size="12" font-family="sans-serif">Vue locale du ciel — cartes indicatives calculées pour 50° N, longitude 4,5° E</text>
{panel(data,0,'7 septembre 2026 — 22 h CEST',2026,9,7,20)}
{panel(data,750,'8 septembre 2026 — 5 h CEST',2026,9,8,3)}
</svg>'''
    (OUT/f'{key}-oriente-22h-5h.svg').write_text(svg, encoding='utf-8')
    print(key, '22h LST', lst_hours(2026,9,7,20), '5h LST', lst_hours(2026,9,8,3))
