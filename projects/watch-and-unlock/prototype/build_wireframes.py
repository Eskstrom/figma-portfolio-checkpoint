"""Build standalone vector wireframes and an offline review prototype. No dependencies."""
from pathlib import Path
from html import escape
import json
import textwrap
import sys
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'screens'
OUT.mkdir(exist_ok=True)
STAGE = sys.argv[1] if len(sys.argv) > 1 else 'full'
BG, PANEL, RAISED, INK, MUTED, LINE, WHITE = '#111111', '#1D1D1D', '#292929', '#F5F5F5', '#B8B8B8', '#555555', '#FFFFFF'
SCREENS = []

class Screen:
    def __init__(self, key, title, balance, note, mobile=False):
        self.key, self.title, self.balance, self.note, self.mobile = key, title, balance, note, mobile
        self.w, self.h = (390, 844) if mobile else (1920, 1080)
        self.items = []
        self.rect(0, 0, self.w, self.h, BG, radius=0)
        if mobile:
            self.text(20, 28, '9:41', 13)
            self.text(296, 28, 'Wi-Fi  100%', 11, color=MUTED)
            self.text(20, 76, 'streamly', 22, bold=True)
            self.text(272, 76, f'{balance} tokens', 13, color=INK)
            self.rule(20, 98, 350)
        else:
            self.text(96, 105, 'streamly', 36, bold=True)
            self.text(302, 105, 'WATCH & UNLOCK', 22, color=MUTED)
            self.rect(1514, 60, 310, 72, PANEL, LINE, 36)
            self.circle(1555, 96, 17, 'none', MUTED)
            self.text(1590, 106, f'{balance} tokens', 28, bold=True)
            self.rule(96, 162, 1728)
            self.text(96, 1015, 'STREAMLY  /  REWARDS PILOT', 20, color=MUTED)
            self.text(1380, 1015, 'Back = return   ·   Select = choose', 20, color=MUTED)

    def rect(self,x,y,w,h,fill=PANEL,stroke=None,radius=16,dash=None):
        attrs = f' fill="{fill}" rx="{radius}"'
        if stroke: attrs += f' stroke="{stroke}" stroke-width="2"'
        if dash: attrs += f' stroke-dasharray="{dash}"'
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{attrs}/>')

    def circle(self,x,y,r,fill,stroke=None):
        self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="2"' if stroke else '')+'/>')

    def rule(self,x,y,w):
        self.items.append(f'<path d="M{x} {y}h{w}" stroke="{LINE}"/>')

    def text(self,x,y,txt,size=26,color=INK,bold=False):
        self.items.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Inter, Arial, sans-serif" font-size="{size}" font-weight="{600 if bold else 400}">{escape(str(txt))}</text>')

    def paragraph(self,x,y,txt,width,size=26,color=MUTED,line=None):
        line = line or round(size*1.4)
        limit = max(12, int(width/(size*.54)))
        for para in txt.split('\n'):
            for row in textwrap.wrap(para, width=limit) or ['']:
                self.text(x,y,row,size,color)
                y += line
        return y

    def button(self,x,y,w,label,action,primary=False,focus=False,small=False,disabled=False):
        h, size = (50,15) if small else (76,26)
        fill = INK if primary and not disabled else PANEL
        if focus: self.rect(x-8,y-8,w+16,h+16,'none',WHITE,18 if not small else 14)
        attrs = f'data-action="{escape(action)}" role="button" tabindex="0" aria-label="{escape(label)}"'
        if disabled: attrs = f'aria-disabled="true" aria-label="{escape(label)}"'
        self.items.append(f'<g {attrs}><title>{escape(label)}</title>')
        self.rect(x,y,w,h,fill,LINE if not primary else None,12)
        self.text(x+20,y+(h+size*.7)/2,label,size, BG if primary and not disabled else (MUTED if disabled else INK),True)
        self.items.append('</g>')

    def pill(self,x,y,label,width=190,small=False):
        h,size = (30,12) if small else (44,20)
        self.rect(x,y,width,h,RAISED,LINE,h/2)
        self.text(x+16,y+(h+size*.7)/2,label,size)

    def media(self,x,y,w,h,label,subtitle='Artwork placeholder',small=False):
        self.rect(x,y,w,h,RAISED,LINE,16)
        self.items.append(f'<path d="M{x+24} {y+24}L{x+w-24} {y+h-24}M{x+w-24} {y+24}L{x+24} {y+h-24}" stroke="#3B3B3B" stroke-width="2"/>')
        self.text(x+24,y+h/2,label,20 if small else 34,bold=True)
        self.text(x+24,y+h/2+34,subtitle,13 if small else 22,color=MUTED)

    def save(self):
        body=''.join(self.items)
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" aria-label="{escape(self.title)}"><title>{escape(self.title)}</title>{body}</svg>'
        (OUT/f'{self.key}.svg').write_text(svg,encoding='utf-8')
        SCREENS.append(dict(id=self.key,title=self.title,balance=self.balance,note=self.note,mobile=self.mobile,svg=svg))

def tv():
    s=Screen('tv-01','Episode complete',5,'Default focus: Play Episode 4. Right moves to the voluntary ad offer. No autoplay countdown in this wireframe.')
    s.pill(96,218,'EPISODE COMPLETE',246)
    s.text(96,348,'One episode down.',64,bold=True)
    s.text(96,422,'A little more unlocked.',64,bold=True)
    s.text(96,490,'Afterlight · Season 1, Episode 3',28,color=MUTED)
    s.rect(96,546,888,96,PANEL,LINE)
    s.text(128,607,'+5 tokens added to your wallet',30,bold=True)
    s.button(104,708,450,'Play Episode 4','play:5',True,True)
    s.button(584,708,360,'View rewards','wallet:5')
    s.text(104,848,'Your next episode is ready whenever you are.',24,color=MUTED)
    s.rect(1112,218,712,686,PANEL,LINE,24)
    s.pill(1152,258,'OPTIONAL SPONSOR AD',286)
    s.text(1152,377,'Earn 15 more tokens',40,bold=True)
    s.paragraph(1152,429,'Watch a 30-second ad from Northstar Audio.',592,28)
    s.media(1152,508,592,156,'NORTHSTAR AUDIO','Sponsor creative placeholder')
    s.button(1152,704,592,'Watch ad · +15 tokens','tv-02',True)
    s.text(1152,835,'No purchase required. Your choice.',24,color=MUTED)
    s.save()

    s=Screen('tv-02','Optional sponsor ad',5,'Prototype simulation: use the review toolbar to complete the ad. Real earning requires confirmed completion. Exit preserves the 5-token balance.')
    s.pill(96,202,'SPONSORED',174)
    s.text(300,233,'Northstar Audio',28,color=MUTED)
    s.pill(1494,202,'EARN 15 TOKENS',300)
    s.media(96,286,1728,466,'NORTHSTAR AUDIO','30-second ad creative · wireframe placeholder')
    s.rect(96,790,1728,6,LINE,radius=3)
    s.rect(96,790,691,6,WHITE,radius=3)
    s.text(96,840,'Ad · 00:18 remaining',26)
    s.text(1140,840,'Complete this ad to earn 15 tokens',26,color=MUTED)
    s.button(96,882,220,'Pause','pause')
    s.button(340,882,250,'Captions','captions')
    s.button(1564,882,260,'Leave ad','edge-exit')
    s.save()

    s=Screen('tv-03','Ad reward confirmed',20,'Continue stays the easiest action. Scanning the QR code does not earn tokens; the optional 10-second demo does.')
    s.pill(96,222,'REWARD CONFIRMED',270)
    s.text(96,358,'15 tokens added.',64,bold=True)
    s.text(96,446,'Your balance is now 20 tokens.',32,color=MUTED)
    s.rect(96,504,888,118,PANEL,LINE)
    s.text(128,554,'5 tokens away from your first ad skip',30,bold=True)
    s.rect(128,582,816,8,LINE,radius=4)
    s.rect(128,582,653,8,WHITE,radius=4)
    s.button(104,708,450,'Play Episode 4','play:20',True,True)
    s.button(584,708,360,'View rewards','wallet:20')
    s.rect(1112,222,712,682,PANEL,LINE,24)
    s.pill(1152,266,'OPTIONAL BONUS',244)
    s.text(1152,376,'One more way to earn.',38,bold=True)
    s.paragraph(1152,443,'Scan with your phone and watch a 10-second Northstar Audio demo.',592,30)
    s.text(1152,594,'+5 tokens',52,bold=True)
    s.button(1152,704,592,'Show QR code','tv-04',True)
    s.text(1152,835,'No purchase or sign-up to the sponsor.',23,color=MUTED)
    s.save()

    s=Screen('tv-04','Continue on your phone',20,'The QR region is deliberately a labeled placeholder. Use “Simulate phone handoff” in the review toolbar. Back returns to TV-03.')
    s.text(96,262,'A quick detour. A small bonus.',52,bold=True)
    s.text(96,319,'Watch the Northstar Audio demo on your phone to earn 5 tokens.',28,color=MUTED)
    s.rect(96,378,1728,554,PANEL,LINE,24)
    s.rect(144,426,400,400,'#EEEEEE',radius=16)
    s.text(184,596,'QR CODE',40,BG,True)
    s.text(184,642,'PLACEHOLDER',30,BG)
    s.text(184,700,'Prototype only · not scannable',18,'#444444')
    s.text(640,461,'1. Scan with your phone',34,bold=True)
    s.text(640,529,'2. Confirm your Streamly account',34,bold=True)
    s.text(640,597,'3. Watch the 10-second demo',34,bold=True)
    s.text(640,675,'Or visit streamly.example/reward · Code DEMO25',25,color=MUTED)
    s.text(640,715,'Fictional address and code for this wireframe.',22,color=MUTED)
    s.pill(640,756,'WAITING FOR YOUR PHONE',388)
    s.button(1416,812,360,'Back to TV','tv-03')
    s.save()

    wallet(25,'tv-05')
    s=Screen('tv-06','Confirm redemption',25,'Default focus: Cancel. Token deduction occurs only after activation succeeds. This reward skips exactly one eligible break.')
    s.rect(432,214,1056,714,PANEL,LINE,24)
    s.pill(480,258,'REVIEW YOUR REWARD',306)
    s.text(480,366,'Skip one ad break?',48,bold=True)
    s.paragraph(480,429,'Use this reward for the next eligible ad break in Afterlight · Season 1, Episode 4.',944,28)
    s.rule(480,515,960)
    s.text(480,569,'Reward cost',28,color=MUTED)
    s.text(1160,569,'25 tokens',32,bold=True)
    s.text(480,629,'Balance after activation',28,color=MUTED)
    s.text(1160,629,'0 tokens',32,bold=True)
    s.paragraph(480,694,'Other ad breaks may still play. If unused for 24 hours, your 25 tokens return automatically.',920,24)
    s.button(488,798,260,'Cancel','tv-05',False,True)
    s.button(788,798,652,'Confirm · 25 tokens','tv-07',True)
    s.save()

    s=Screen('tv-07','Reward activated',0,'25 tokens spent. The benefit is reserved for Episode 4. The prototype toolbar can simulate delivery at the next eligible break.')
    s.pill(96,222,'REWARD ACTIVATED',264)
    s.text(96,354,'Your ad-break skip',64,bold=True)
    s.text(96,429,'is ready.',64,bold=True)
    s.text(96,505,'Reserved for Afterlight · Episode 4',30,color=MUTED)
    s.rect(96,562,888,98,PANEL,LINE)
    s.text(128,624,'25 tokens used   ·   New balance: 0 tokens',28,bold=True)
    s.button(104,738,450,'Play Episode 4','play:reserved',True,True)
    s.button(584,738,360,'Token activity','tv-08')
    s.media(1112,222,712,492,'AFTERLIGHT','Season 1 · Episode 4')
    s.paragraph(1112,785,'Your next eligible ad break will be skipped automatically.',660,28)
    s.save()

    s=Screen('tv-08','Token activity',0,'Account wallet. Each transaction identifies profile and status. Reserved changes to Applied after the break is skipped.')
    s.text(96,269,'Every token, accounted for.',52,bold=True)
    s.text(96,326,'Today · Alex’s profile · Account wallet',26,color=MUTED)
    rows=[('Afterlight · Episode 3 completed','+5','EARNED','8:42 PM'),('Northstar Audio ad completed','+15','EARNED','8:43 PM'),('Northstar Audio demo completed','+5','EARNED','8:44 PM'),('Ad-break skip · Afterlight Episode 4','−25','RESERVED','8:45 PM')]
    for i,(title,amount,status,time) in enumerate(rows):
        y=382+i*122
        s.rect(96,y,1728,102,PANEL,LINE,12)
        s.text(128,y+42,title,28,bold=True)
        s.text(128,y+78,f'Alex · {time}',22,color=MUTED)
        s.text(1310,y+58,status,22,color=MUTED)
        s.text(1628,y+59,amount,34,bold=True)
    s.button(96,898,300,'Back to reward','tv-07')
    s.save()

def wallet(balance,key):
    s=Screen(key,'Wallet and rewards' if balance==25 else 'Wallet · more tokens needed',balance,'Reward availability is checked for Episode 4. Prices are illustrative. HD and other premium rewards are a future exploration.')
    s.text(96,272,'Make your next episode better.',52,bold=True)
    s.text(96,330,'A little attention. A reward you choose.',28,color=MUTED)
    s.rect(96,394,1024,470,PANEL,LINE,24)
    s.pill(136,434,'AVAILABLE FOR EPISODE 4',358)
    s.text(136,551,'Skip one ad break',44,bold=True)
    s.paragraph(136,607,'The next eligible ad break in Afterlight · Episode 4. Other breaks may still play.',928,27)
    if balance>=25:
        s.button(144,746,610,'Use 25 tokens','tv-06',True,True)
    else:
        s.button(136,730,620,f'{25-balance} more tokens needed','none',disabled=True)
    s.rect(1184,394,640,470,PANEL,LINE,24)
    s.text(1224,466,'YOUR WALLET',22,color=MUTED)
    s.text(1224,558,str(balance),84,bold=True)
    s.text(1224,608,'tokens available',28,color=MUTED)
    s.rule(1224,652,560)
    s.paragraph(1224,704,'Platform credits. No cash value. Tokens do not expire in this pilot.',540,24)
    s.button(96,894,380,'Continue watching',f'play:{balance}')
    s.button(506,894,420,'See ways to earn','tv-03' if balance==20 else 'tv-01')
    s.save()

def mobile():
    s=Screen('m-01','Confirm account on phone',20,'Signed-in account shown only after authentication. “Use another account” opens the sign-in variant.',True)
    s.pill(20,118,'SPONSORED · NORTHSTAR AUDIO',280,True)
    s.text(20,190,'A closer look.',30,bold=True)
    s.text(20,230,'5 more tokens.',30,bold=True)
    s.paragraph(20,270,'Watch a 10-second product demo to earn your bonus.',346,16)
    s.media(20,334,350,166,'NORTHSTAR AUDIO','Product image placeholder',True)
    s.rect(20,524,350,104,PANEL,LINE,12)
    s.text(36,555,'Credit tokens to Alex’s account?',16,bold=True)
    s.text(36,584,'Streamly account confirmed',14,color=MUTED)
    s.text(20,658,'No purchase or sponsor registration required.',13,color=MUTED)
    s.button(20,684,350,'Confirm and watch demo','m-02',True,small=True)
    s.button(20,750,350,'Use another account','m-signin',small=True)
    s.save()

    s=Screen('m-02','Watch sponsor demo',20,'Review toolbar simulates completion. Playback controls are illustrative; this wireframe has no real video.',True)
    s.pill(20,118,'SPONSORED · NORTHSTAR AUDIO',280,True)
    s.text(20,190,'Meet your next listen.',28,bold=True)
    s.paragraph(20,233,'Your bonus unlocks when this 10-second demo finishes.',344,16)
    s.media(20,300,350,224,'PRODUCT DEMO','10-second video placeholder',True)
    s.rect(20,547,350,4,LINE,radius=2)
    s.rect(20,547,140,4,WHITE,radius=2)
    s.text(20,577,'00:06 remaining',14,color=MUTED)
    s.button(20,601,160,'Pause','pause',small=True)
    s.button(198,601,172,'Captions','captions',small=True)
    s.paragraph(20,691,'Exploring the sponsor website is optional and earns no extra tokens.',346,15)
    s.button(20,752,350,'Visit sponsor website ↗','sponsor',small=True)
    s.save()

    s=Screen('m-03','Mobile bonus confirmed',25,'Bonus is credited once per qualifying ad session. “Return to TV” in the review toolbar simulates cross-device sync.',True)
    s.pill(20,122,'BONUS CONFIRMED',194,True)
    s.circle(195,266,58,PANEL,LINE)
    s.text(153,282,'+5',48,bold=True)
    s.text(20,399,'5 tokens added.',32,bold=True)
    s.paragraph(20,445,'Your balance is now 25 tokens. Your TV wallet will update automatically.',344,17)
    s.rect(20,539,350,100,PANEL,LINE,12)
    s.text(36,575,'Your first ad skip is within reach.',16,bold=True)
    s.text(36,608,'Use 25 tokens from Rewards on your TV.',14,color=MUTED)
    s.button(20,686,350,'Done','mobile-done',True,small=True)
    s.button(20,752,350,'Explore Northstar Audio ↗','sponsor',small=True)
    s.save()

    s=Screen('m-signin','Sign in to claim tokens',20,'Authentication is simulated. No passwords are collected or sent anywhere.',True)
    s.text(20,183,'Keep your bonus',30,bold=True)
    s.text(20,223,'with your account.',30,bold=True)
    s.paragraph(20,274,'Sign in to Streamly to confirm where your 5 bonus tokens should go.',344,17)
    s.rect(20,386,350,60,PANEL,LINE,12)
    s.text(36,423,'Email address',16,color=MUTED)
    s.rect(20,462,350,60,PANEL,LINE,12)
    s.text(36,499,'Password',16,color=MUTED)
    s.text(20,560,'Prototype fields · no information is collected',13,color=MUTED)
    s.button(20,618,350,'Simulate sign-in as Alex','m-01',True,small=True)
    s.button(20,690,350,'Cancel','tv-04',small=True)
    s.save()

def edge(key,title,balance,heading,body,primary,action,secondary='Continue watching',secondary_action=None):
    s=Screen(key,title,balance,body)
    s.rect(432,278,1056,598,PANEL,LINE,24)
    s.pill(480,326,title.upper(),min(760,len(title)*16+50))
    s.text(480,454,heading,46,bold=True)
    s.paragraph(480,520,body,920,29)
    s.button(480,716,480,primary,action,True)
    s.button(990,716,450,secondary,secondary_action or f'play:{balance}')
    s.save()

def extras():
    wallet(20,'edge-wallet-20')
    wallet(5,'edge-wallet-5')
    wallet(0,'edge-wallet-0')
    edge('edge-exit','Leave ad',5,'Leave this ad?','You won’t earn the 15 ad tokens. Your 5 existing tokens are safe.','Keep watching','tv-02','Leave ad','play:5')
    edge('edge-pending','Reward pending',5,'Ad complete. Confirming tokens.','Your 15 ad tokens are pending. Your spendable balance stays at 5 tokens until confirmation.','View pending activity','edge-pending-activity')
    edge('edge-pending-activity','Pending activity',5,'15 ad tokens · Pending','Northstar Audio · Alex’s profile. The ad finished; confirmation is still in progress. No additional action is needed.','Back to reward status','edge-pending')
    edge('edge-expired','QR code expired',20,'Let’s get you a fresh code.','This claim code has expired. Your 20 tokens are safe. Generate a new code to continue with the optional demo.','Generate new code','tv-04')
    edge('edge-unavailable','No reward ads',5,'No reward ads right now.','Your episode tokens are safe. You can continue watching and check for optional reward ads another time.','Continue watching','play:5','View rewards','wallet:5')
    edge('edge-refund','Reward refunded',25,'25 tokens returned.','Your ad-break skip for Afterlight · Episode 4 wasn’t used within 24 hours. The tokens are available again.','View rewards','tv-05','Continue watching','play:25')
    edge('edge-failed','Activation failed',25,'Your reward didn’t activate.','No tokens were spent. Your balance is still 25 tokens. Try again or return to your rewards.','Try again','tv-06','Back to rewards','tv-05')
    for bal,status in [(0,'none'),(5,'none'),(20,'none'),(25,'none'),(0,'reserved'),(0,'applied')]:
        key=f'play-{status}' if status!='none' else f'play-{bal}'
        s=Screen(key,'Episode 4 playback'+(' · '+status if status!='none' else ''),bal,'Playback artwork and delivery are simulated. Use the review toolbar to apply a reserved ad-break skip.')
        s.media(96,212,1728,576,'AFTERLIGHT','Season 1 · Episode 4 · playback placeholder')
        if status!='none': s.pill(136,254,'AD-BREAK SKIP '+('READY' if status=='reserved' else 'APPLIED'),430)
        s.text(96,856,'Afterlight · Episode 4',32,bold=True)
        s.text(1150,856,'Ad break skipped with tokens' if status=='applied' else 'Your next episode is playing',26,color=MUTED)
        s.button(96,890,400,'Back to rewards','tv-07' if status=='reserved' else f'wallet:{bal}')
        s.save()

def write_preview():
    payload=json.dumps(SCREENS,ensure_ascii=False).replace('</',r'<\/')
    template='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Watch & Unlock — Wireframe review</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#e9e8e4;color:#171717;font:15px Arial,sans-serif}button,a{font:inherit}button{cursor:pointer}button:focus-visible,a:focus-visible{outline:3px solid #42628a;outline-offset:3px}header{padding:24px 32px;border-bottom:1px solid #c7c7c3;background:#f7f7f3;display:flex;justify-content:space-between;gap:20px;align-items:center}h1{font-size:22px;margin:5px 0 0}.eyebrow{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#666}.tag{border:1px solid #aaa;border-radius:20px;padding:8px 12px;font-size:12px}main{display:grid;grid-template-columns:245px 1fr;min-height:calc(100vh - 95px)}nav{padding:22px 14px;border-right:1px solid #c7c7c3;max-height:calc(100vh - 95px);overflow:auto;position:sticky;top:0}nav h2{font-size:11px;letter-spacing:1px;text-transform:uppercase;margin:20px 12px 8px;color:#666}nav button{display:block;width:100%;border:0;background:transparent;text-align:left;padding:12px;border-radius:6px;color:#444;font-size:13px}nav button.active{background:#242424;color:white}nav small{display:block;opacity:.7;margin-top:4px;font-size:11px}.workspace{padding:24px 28px}.toolbar{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:16px}.toolbar h2{font-size:19px;margin:0}.toolbar p{font-size:12px;color:#666;margin:6px 0 0}.controls{display:flex;gap:8px;flex-wrap:wrap}.controls button,.controls a{border:1px solid #aaa;background:#f8f8f5;color:#222;border-radius:6px;padding:9px 12px;font-size:12px;text-decoration:none}.canvas{background:#d5d5d0;border:1px solid #bebeb9;border-radius:10px;padding:20px;min-height:460px;display:flex;align-items:center;justify-content:center}.canvas svg{display:block;width:100%;height:auto;max-height:75vh}.canvas.mobile svg{width:390px;max-width:100%;max-height:75vh}.canvas svg [data-action]{cursor:pointer}.canvas svg [data-action]:focus{outline:none;filter:drop-shadow(0 0 5px white)}.notes{margin-top:16px;display:grid;grid-template-columns:1fr 300px;gap:24px;font-size:13px;line-height:1.6}.notes p{margin:6px 0}.simulation{border-top:1px solid #bbb;padding-top:12px;margin-top:14px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}.simulation span{font-size:12px;color:#555;margin-right:8px}.simulation button{padding:8px 12px;border:1px dashed #777;background:transparent;border-radius:6px;font-size:12px}#toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);background:#151515;color:white;padding:14px 22px;border-radius:8px;max-width:90%;z-index:3;display:none}.meta{font-size:12px;color:#555}.balance{font-size:24px;display:block;font-weight:bold}.disclaimer{font-size:12px;color:#555;border-top:1px solid #ccc;margin-top:14px;padding-top:12px}.flow{font-size:12px;color:#666;margin:8px 0 18px;line-height:1.6}@media(max-width:850px){main{grid-template-columns:1fr}nav{position:static;max-height:180px;border-bottom:1px solid #bbb}header{padding:18px}.workspace{padding:16px}.toolbar{align-items:flex-start;flex-direction:column}.notes{grid-template-columns:1fr}.canvas{min-height:230px;padding:8px}}@media print{header,nav,.toolbar,.simulation,.notes{display:none}main{display:block}.workspace,.canvas{padding:0;border:0;background:white}.canvas svg{max-height:none}}
</style></head><body><header><div><div class="eyebrow">Product concept / Interaction wireframes</div><h1>Watch & Unlock</h1></div><span class="tag">Saved locally · v1 · grayscale</span></header><main><nav id="nav" aria-label="Wireframe screens"></nav><section class="workspace"><div class="toolbar"><div><h2 id="title"></h2><p id="screen-id"></p></div><div class="controls"><button id="back">← Back</button><button id="restart">Restart journey</button><a id="download" download>Download SVG</a><button onclick="window.print()">Print screen</button></div></div><div class="flow">Episode +5 → Optional ad +15 → Sponsor demo +5 → Wallet 25 → One ad-break skip −25 → Balance 0</div><div id="canvas" class="canvas"></div><div class="simulation" id="simulation"></div><div class="notes"><div><strong>Interaction notes</strong><p id="note"></p><p class="disclaimer">Click screen buttons to explore. Tab moves through controls; Enter or Space selects. Escape goes back. Media, QR handoff, sign-in, and reward confirmation are simulated. No real ads, accounts, or transactions.</p></div><div><span class="meta">SPENDABLE BALANCE ON THIS SCREEN</span><span class="balance" id="balance"></span><p class="meta">Sample prices for concept testing. One ad-break skip is not a full ad-free episode.</p></div></div></section></main><div id="toast" role="status"></div><script>
const screens=__DATA__;
const map=Object.fromEntries(screens.map(s=>[s.id,s]));
let current='tv-01',historyStack=[],timer;const canvas=document.querySelector('#canvas');
function toast(t){let el=document.querySelector('#toast');el.textContent=t;el.style.display='block';clearTimeout(timer);timer=setTimeout(()=>el.style.display='none',4200)}
function render(id,push=true){if(!map[id]){toast('This screen is in the next saved milestone.');return}if(push&&current!==id)historyStack.push(current);current=id;let s=map[id];document.querySelector('#title').textContent=s.title;document.querySelector('#screen-id').textContent=s.id.toUpperCase()+' / '+(s.mobile?'MOBILE · 390 × 844':'TV · 1920 × 1080');document.querySelector('#balance').textContent=s.balance+' tokens';document.querySelector('#note').textContent=s.note;canvas.innerHTML=s.svg;canvas.classList.toggle('mobile',s.mobile);document.querySelector('#download').href='screens/'+s.id+'.svg';document.querySelectorAll('nav button').forEach(b=>b.classList.toggle('active',b.dataset.id===id));let sim=[];
if(id==='tv-02')sim=[['Simulate ad complete','tv-03'],['Simulate pending reward','edge-pending']];
if(id==='tv-04')sim=[['Simulate phone handoff','m-01'],['Simulate expired code','edge-expired']];
if(id==='m-02')sim=[['Simulate demo complete','m-03']];
if(id==='m-03')sim=[['Return to TV · wallet synced','tv-05']];
if(id==='tv-06')sim=[['Simulate activation failure','edge-failed']];
if(id==='play-reserved')sim=[['Simulate next eligible break','play-applied'],['Simulate unused for 24 hours','edge-refund']];
if(id==='edge-pending'||id==='edge-pending-activity')sim=[['Simulate credit confirmed','tv-03']];
let target=document.querySelector('#simulation');target.replaceChildren();let label=document.createElement('span');label.textContent='REVIEW CONTROLS · outside product';target.append(label);for(let [name,dest] of sim){let b=document.createElement('button');b.textContent=name;b.onclick=()=>render(dest);target.append(b)}if(!sim.length){let t=document.createElement('span');t.textContent='Select a screen action to continue.';target.append(t)}try{localStorage.setItem('watch-unlock-review',id)}catch{} }
function action(a){if(a.startsWith('play:')){let k=a.split(':')[1];render('play-'+k);return}if(a.startsWith('wallet:')){let b=+a.split(':')[1];render(b>=25?'tv-05':b===20?'edge-wallet-20':b===5?'edge-wallet-5':'edge-wallet-0');return}if(a==='pause'){toast('Playback pause/resume simulated. No real video is loaded.');return}if(a==='captions'){toast('Captions control selected. Captioned media is required in production.');return}if(a==='sponsor'){toast('Fictional sponsor destination. No external site is opened.');return}if(a==='mobile-done'){toast('You’re done on your phone. Use “Return to TV” above to simulate wallet sync.');return}render(a)}
canvas.addEventListener('click',e=>{let b=e.target.closest('[data-action]');if(b)action(b.dataset.action)});canvas.addEventListener('keydown',e=>{let b=e.target.closest('[data-action]');if(b&&(e.key==='Enter'||e.key===' ')){e.preventDefault();action(b.dataset.action)}});
function back(){let prev=historyStack.pop();if(prev)render(prev,false)}document.querySelector('#back').onclick=back;document.querySelector('#restart').onclick=()=>{historyStack=[];render('tv-01',false)};document.addEventListener('keydown',e=>{if(e.key==='Escape')back()});
let nav=document.querySelector('#nav');for(let [label,fn]of[['TV journey',s=>s.id.startsWith('tv-')],['Mobile handoff',s=>s.mobile],['Edge states',s=>s.id.startsWith('edge-')],['Playback states',s=>s.id.startsWith('play-')]]){let group=screens.filter(fn);if(!group.length)continue;let h=document.createElement('h2');h.textContent=label;nav.append(h);for(let s of group){let b=document.createElement('button');b.dataset.id=s.id;b.textContent=s.title;let small=document.createElement('small');small.textContent=s.id.toUpperCase()+' · '+s.balance+' tokens';b.append(small);b.onclick=()=>render(s.id);nav.append(b)}}render('tv-01',false);
</script></body></html>'''
    (ROOT/'index.html').write_text(template.replace('__DATA__',payload),encoding='utf-8')

def save_docs():
    manifest={
      'version':'1.0','stage':STAGE,'screen_count':len(SCREENS),
      'figma_file':'https://www.figma.com/design/R6I5AHFaQCs4r7FltVYoi6',
      'figma_status':'Blank file created; further connector operations blocked by Starter-plan MCP limit.',
      'screens':[{k:v for k,v in s.items() if k!='svg'} for s in SCREENS]}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
    rows='\n'.join(f"| {s['id']} | {s['title']} | {s['balance']} |" for s in SCREENS)
    (ROOT/'README.md').write_text(f'''# Watch & Unlock — Wireframes v1

Saved local wireframe package based on the Watch & Unlock case study. **{len(SCREENS)} vector screens** in the {STAGE} milestone.

## Open and review

Open `index.html` in a browser. It works offline and contains every screen. Click product buttons to follow the flow; use the labeled review controls to simulate ad completion, mobile handoff, and cross-device confirmation. Use Tab / Enter / Space for accessible selection and Escape to go back. This is a click-through prototype; production TV directional-focus handling is not implemented.

The canonical balance is **5 → 20 → 25 → 0**. Restart the journey from the toolbar. The sidebar also opens individual screen states for review; jumping via the sidebar is not a real transaction.

## Import into Figma

1. Open the [created Figma file](https://www.figma.com/design/R6I5AHFaQCs4r7FltVYoi6).
2. Drag the SVGs from `screens/` onto the canvas. TV artboards are 1920 × 1080; mobile artboards are 390 × 844.
3. Group TV-01 through TV-08 in order. Put mobile screens beneath the QR handoff and edge states in a separate row.
4. The SVGs contain vector shapes and text. Depending on Figma’s importer and installed fonts, text may be outlined; inspect it before editing. SVG import does not create Auto Layout, component variants, or prototype connections.
5. Recreate shared buttons, balance pills, notices, and cards as native Figma components using the specifications in the case study. Use Inter if available; the preview falls back to Arial offline.
6. Wire the main path: TV-01 → TV-02 → TV-03 → TV-04 → M-01 → M-02 → M-03 → TV-05 → TV-06 → TV-07 → Play-reserved → Play-applied.

The Figma file was created successfully, but the connector hit its Starter-plan MCP tool limit before design nodes could be added. **The wireframes are saved locally, not inside that Figma file.**

## What is simulated

All artwork, ads, video playback, QR codes, authentication, sponsor destinations, rewards, and synchronization. No credentials are collected. No network services are required by the prototype. Token prices and eligibility rules are concept assumptions, not validated commercial terms.

## Saved progress

`checkpoints/01-tv/` preserves the first eight TV screens and review page. `checkpoints/02-complete/` preserves the completed journey, mobile handoff, and recovery states. Checkpoints are local file copies, not Git commits or Figma version history.

## Screen inventory

| Screen | Purpose | Spendable tokens |
| --- | --- | ---: |
{rows}

## Source and regeneration

`build_wireframes.py` uses Python’s standard library. Run `python build_wireframes.py tv` for the TV milestone, or `python build_wireframes.py full` for the full package. Screens use named groups, reusable drawing helpers, and a consistent grayscale style. The generator preserves milestone directories and creates a ZIP for sharing.
''',encoding='utf-8')

tv()
if STAGE!='tv':
    mobile()
    extras()
write_preview()
save_docs()
checkpoint=ROOT/'checkpoints'/({'tv':'01-tv','full':'02-complete','verified':'03-verified'}[STAGE])
checkpoint.mkdir(parents=True,exist_ok=True)
for file in ['index.html','manifest.json','README.md']:
    shutil.copy2(ROOT/file,checkpoint/file)
(checkpoint/'screens').mkdir(exist_ok=True)
for s in SCREENS:
    shutil.copy2(OUT/f"{s['id']}.svg",checkpoint/'screens'/f"{s['id']}.svg")
with zipfile.ZipFile(ROOT/'watch-and-unlock-wireframes.zip','w',zipfile.ZIP_DEFLATED) as z:
    for file in ['index.html','manifest.json','README.md','build_wireframes.py']:
        z.write(ROOT/file,file)
    for s in SCREENS: z.write(OUT/f"{s['id']}.svg",f"screens/{s['id']}.svg")
print(json.dumps({'stage':STAGE,'screens':len(SCREENS),'checkpoint':str(checkpoint),'preview':str(ROOT/'index.html')},indent=2))
