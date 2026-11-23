import hashlib, json, re, qrcode, html, os, shutil
BASE = 'https://drvitpd.github.io/npaes-textbook/'
CODE = 'NPAES2565'
norm = lambda s: re.sub(r'[\s\-]', '', s).upper()
H = hashlib.sha256(norm(CODE).encode()).hexdigest()
TITLE = 'TFRS for NPAEs: หลักการและการประยุกต์ใช้ (ฉบับปรับปรุง 2565)'
SUB = 'การบัญชีตามมาตรฐานการรายงานทางการเงินสำหรับกิจการที่ไม่มีส่วนได้เสียสาธารณะ'
APPS = os.environ.get('APPS', '/home/claude/npaes-apps/apps')
T = {1:'ความเป็นมาและวัตถุประสงค์',2:'ขอบเขตและนิยาม NPAEs',3:'กรอบแนวคิดการรายงานทางการเงิน',4:'การนำเสนองบการเงิน',5:'นโยบายบัญชี ประมาณการ และข้อผิดพลาด',6:'เงินสดและรายการเทียบเท่าเงินสด',7:'ลูกหนี้',8:'สินค้าคงเหลือ',9:'เงินลงทุน',10:'ที่ดิน อาคารและอุปกรณ์',11:'สินทรัพย์ไม่มีตัวตน',12:'อสังหาริมทรัพย์เพื่อการลงทุน',13:'ต้นทุนการกู้ยืม',14:'สัญญาเช่า',15:'ภาษีเงินได้',16:'ประมาณการหนี้สินและหนี้สินที่อาจเกิดขึ้น',17:'เหตุการณ์ภายหลังรอบระยะเวลารายงาน',18:'รายได้',19:'รายได้จากการขายอสังหาริมทรัพย์',20:'สัญญาก่อสร้าง',21:'ผลกระทบจากอัตราแลกเปลี่ยน',22:'เกษตรกรรม',23:'เงินอุดหนุนจากรัฐบาล',24:'อนุพันธ์',25:'การรวมธุรกิจ',26:'การสำรวจและประเมินค่าแหล่งทรัพยากรแร่',27:'ข้อตกลงสัมปทานบริการ',28:'วันถือปฏิบัติและการเปลี่ยนผ่าน',29:'รูปแบบรายการย่อของงบการเงิน',30:'การบัญชีสำหรับองค์กรไม่แสวงหากำไร'}
GATE = '''<style>#gate{position:fixed;inset:0;background:#F2F7FB;z-index:99999;display:flex;align-items:center;justify-content:center;font-family:Sarabun,'Noto Sans Thai',sans-serif}
#gate .gb{background:#fff;border-top:4px solid #1F3864;border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,.08);padding:28px 26px;max-width:380px;width:88%;color:#222}
#gate h2{color:#1F3864;font-size:19px;margin:0 0 6px}#gate p{font-size:14px;margin:0 0 14px;line-height:1.6}
#gate .row{display:flex;gap:6px}#gate input[type=password],#gate input[type=text]{flex:1;font-size:16px;padding:9px 10px;border:1px solid #b8c4d4;border-radius:6px}
#gate button{font-family:inherit;font-size:15px;border:0;border-radius:6px;padding:9px 14px;cursor:pointer}#gate .sh{background:#E3E9F1;color:#1F3864}#gate .go{background:#1F3864;color:#fff;width:100%;margin-top:12px}
#gate label{font-size:13px;display:flex;gap:6px;align-items:center;margin-top:10px}#gate .err{color:#A93226;font-size:13px;min-height:18px;margin-top:8px}</style>
<div id="gate"><div class="gb"><img src="logo-drvitpd.png" alt="Dr.VIT &amp; PD" style="height:46px;max-width:100%;margin-bottom:6px"><h2>แอปประจำตำรา</h2><p>สำหรับผู้อ่านตำรา<br><b>''' + TITLE + '''</b><br>ใส่รหัสเข้าแอปที่พิมพ์ไว้ในตำรา</p>
<div class="row"><input id="gk" type="password" autocomplete="off" placeholder="รหัสเข้าแอป"><button class="sh" type="button" onclick="var i=document.getElementById('gk');i.type=i.type==='password'?'text':'password'">แสดง</button></div>
<label><input id="gr" type="checkbox"> จำรหัสในเครื่องนี้</label><button class="go" type="button" id="gg">เปิดแอป</button><div class="err" id="ge"></div></div></div>
<script>(function(){var H="''' + H + '''",K="npaes_gate";
function ok(){var g=document.getElementById('gate');if(g)g.remove();}
try{if(localStorage.getItem(K)===H||sessionStorage.getItem(K)===H){ok();return;}}catch(e){}
async function chk(){var v=document.getElementById('gk').value.replace(/[\\s\\-]/g,'').toUpperCase();
var b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(v));var h=Array.from(new Uint8Array(b)).map(function(x){return x.toString(16).padStart(2,'0')}).join('');
if(h===H){try{(document.getElementById('gr').checked?localStorage:sessionStorage).setItem(K,H)}catch(e){}ok();}else{document.getElementById('ge').textContent='รหัสไม่ถูกต้อง โปรดดูรหัสที่พิมพ์ไว้ในตำรา';}}
document.getElementById('gg').onclick=chk;document.getElementById('gk').addEventListener('keydown',function(e){if(e.key==='Enter')chk();});})();</script>'''
NAV = '<div style="font-family:Sarabun,sans-serif;font-size:13px;padding:6px 14px;background:#fff;border-bottom:3px solid #1F3864;display:flex;align-items:center;justify-content:space-between;gap:10px"><a href="index.html" style="color:#1F3864;text-decoration:none;font-weight:700">← สารบัญแอปประจำตำรา</a><img src="logo-drvitpd.png" alt="Dr.VIT &amp; PD" style="height:26px"></div>'
os.makedirs('docs/qr', exist_ok=True)
MOB = '<style>@media (max-width:640px){body *{min-width:0}table{display:block;overflow-x:auto;max-width:100%}th,td{white-space:normal}select,input,img,svg{max-width:100%}}</style>'
for n in T:
    s = open(f'{APPS}/ch{n:02d}.html', encoding='utf8').read()
    if re.search(r'<body[^>]*>', s): s = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + GATE + NAV, s, count=1)
    elif '</head>' in s: s = s.replace('</head>', '</head><body>' + GATE + NAV, 1) + ('' if '</body>' in s else '</body></html>')
    else: s = '<!doctype html><html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + GATE + NAV + s + '</body></html>'
    s = s.replace('</head>', MOB + '</head>', 1) if '</head>' in s else MOB + s
    assert 'id="gate"' in s, n
    open(f'docs/ch{n:02d}.html', 'w', encoding='utf8').write(s)
    q = qrcode.QRCode(border=1, box_size=10); q.add_data(f'{BASE}ch{n:02d}.html#S{n}.1'); q.make(fit=True)
    q.make_image(fill_color='black', back_color='white').save(f'docs/qr/ch{n:02d}.png')
groups = [('ส่วนที่ 1 หลักการและการนำเสนอ', range(1, 6)), ('ส่วนที่ 2 สินทรัพย์และหนี้สิน', range(6, 18)), ('ส่วนที่ 3 รายได้และรายการเฉพาะ', range(18, 22)), ('ส่วนที่ 4 บทใหม่ในฉบับปรับปรุง 2565', range(22, 28)), ('ส่วนที่ 5 การถือปฏิบัติ รายการย่อ และองค์กรไม่แสวงหากำไร', range(28, 31))]
items = ''
for g, chs in groups:
    items += f'<h3>{g}</h3>' + ''.join(f'<a class="c" href="ch{n:02d}.html"><b>บทที่ {n}</b><span>{html.escape(T[n])}</span></a>' for n in chs)
idx = f"""<!DOCTYPE html><html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>แอปประจำตำรา TFRS for NPAEs</title><link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap" rel="stylesheet">
<style>body{{margin:0;font-family:Sarabun,sans-serif;background:#F2F7FB;color:#222}}.w{{max-width:760px;margin:0 auto;padding:22px 16px 40px}}
.hd{{background:#fff;border-radius:10px;padding:18px 20px;border-top:4px solid #1F3864}}.hd img{{height:54px}}h1{{color:#1F3864;font-size:23px;margin:10px 0 2px;line-height:1.35}}.s{{color:#1F3864}}
.how{{background:#fff;border-left:4px solid #F39C12;border-radius:6px;padding:10px 14px;margin:14px 0;font-size:15px;line-height:1.65}}
h3{{color:#1F3864;margin:18px 0 6px;font-size:16px;border-bottom:1px solid #C9D3E0;padding-bottom:3px}}
a.c{{display:flex;gap:12px;background:#fff;border-radius:8px;padding:10px 14px;margin:6px 0;text-decoration:none;color:#222;box-shadow:0 1px 3px rgba(0,0,0,.05)}}a.c b{{color:#1F3864;white-space:nowrap}}
.ft{{color:#777;font-size:12.5px;margin-top:26px;line-height:1.6}}</style></head><body>{GATE}<div class="w">
<div class="hd"><img src="logo-drvitpd.png" alt="Dr.VIT &amp; PD"><h1>{TITLE}</h1><div class="s">{SUB}</div><div style="margin-top:8px;font-weight:700">ดร.วิทยา อรุณศิริเพ็ชร · อ.พงษ์ธร ดวงปัญญา</div></div>
<div class="how">แอปประจำบทใช้คู่กับตำรา สแกนคิวอาร์โค้ดหน้าเปิดบทเพื่อเปิดแท็บเนื้อหาเสริมของบทนั้นทันที แต่ละแอปมีกระดาษทำการ แบบทดสอบ และเนื้อหาเสริม S ที่ย้ายออกจากเล่มพิมพ์ ข้อมูลที่กรอกประมวลผลในเบราว์เซอร์เท่านั้น ชื่อกิจการในตัวอย่างเป็นชื่อสมมติ</div>
{items}<div class="ft">เนื้อหาเป็นการถอดความของคณะผู้เขียน ไม่ใช่ถ้อยคำของมาตรฐาน · ข้อมูลเป็นปัจจุบัน ณ วันที่ 23 พฤศจิกายน 2569</div></div></body></html>"""
open('docs/index.html', 'w', encoding='utf8').write(idx)
open('docs/.nojekyll', 'w').write('')
open('README.md', 'w', encoding='utf8').write(f'# แอปประจำตำรา {TITLE}\n\n{SUB}\n\nผู้เขียน: ดร.วิทยา อรุณศิริเพ็ชร และ อ.พงษ์ธร ดวงปัญญา\n\nเว็บ: {BASE}\n\nแอปประจำบท 30 บท (docs/ch01.html–ch30.html) QR หน้าเปิดบทชี้ chNN.html#SNN.1 (docs/qr/chNN.png)\n')
print('ok', H[:12])
