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
        ],
        'lines': [(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,6)],
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
        ],
        'lines': [(2,3),(3,4),(4,5),(5,2),(4,6),(6,0),(0,1)],
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
        'lines': [(0,1),(1,2),(2,5),(5,4),(4,3),(3,6),(6,0)],
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

for key,data in stars.items():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1450 510" role="img" aria-label="{data['title']} le 7 septembre 2026 à 22 heures et le 8 septembre à 5 heures en Belgique">
<rect width="1450" height="510" fill="#030914"/>
<text x="725" y="18" text-anchor="middle" fill="#dce9ff" font-size="12" font-family="sans-serif">Vue locale du ciel — cartes indicatives calculées pour 50° N, longitude 4,5° E</text>
{panel(data,0,'7 septembre 2026 — 22 h CEST',2026,9,7,20)}
{panel(data,750,'8 septembre 2026 — 5 h CEST',2026,9,8,3)}
</svg>'''
    (OUT/f'{key}-oriente-22h-5h.svg').write_text(svg, encoding='utf-8')
    print(key, '22h LST', lst_hours(2026,9,7,20), '5h LST', lst_hours(2026,9,8,3))
