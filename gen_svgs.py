import os
import base64
import urllib.request

def fetch_image_as_base64(url):
    print(f"Fetching {url[:30]}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read()
            b64 = base64.b64encode(data).decode('utf-8')
            mime = "image/png"
            if data.startswith(b'\xff\xd8'): mime = "image/jpeg"
            elif data.startswith(b'GIF8'): mime = "image/gif"
            return f"data:{mime};base64,{b64}"
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def wrap_svg(width, height, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <style>
        .font-mono {{ font-family: "Courier New", Courier, monospace; }}
        .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
        .pulse {{ animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
    </style>
    <rect width="100%" height="100%" fill="#131313"/>
    {content}
</svg>'''

def draw_retro_bevel(x, y, w, h, bg_color, is_inset=False, thickness=2):
    top_left = "#0e0e0e" if is_inset else "#3a4a49"
    bottom_right = "#3a4a49" if is_inset else "#0e0e0e"
    
    return f'''
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg_color}" />
    <!-- Borders -->
    <rect x="{x}" y="{y}" width="{w}" height="{thickness}" fill="{top_left}" />
    <rect x="{x}" y="{y}" width="{thickness}" height="{h}" fill="{top_left}" />
    <rect x="{x}" y="{y+h-thickness}" width="{w}" height="{thickness}" fill="{bottom_right}" />
    <rect x="{x+w-thickness}" y="{y}" width="{thickness}" height="{h}" fill="{bottom_right}" />
    '''

def generate_hero():
    print("Generating hero.svg...")
    width = 800
    height = 360
    
    avatar_url = "https://lh3.googleusercontent.com/aida-public/AB6AXuDPRZsy7KJlEUu228hzoIKh4sr8rkOh8AZC-UmAfNFyawefHP6870yvn-1rJD9teFf4iWSkn3nbRGr_fqdRxaTJx8d6WeIfIshOnH4DdsIfH7EJ-07UzGN85J4ryv17stbTyB6hhqCHaViujkx6Rvv7RSMTRtiB-WcMejuHAsX5Vn-mTOC5AcxCVD8BgM51KmmsuUGj-MUBPsw7qSjEP_VOwjjpBAdvdOAzaI0ESAp8q3NJQFBqf3zUE-jBJkK1CNXZyQ"
    avatar_b64 = fetch_image_as_base64(avatar_url)
    
    content = f'''
    <!-- Outer Window -->
    {draw_retro_bevel(0, 0, width, height, "#2a2a2a", False, 2)}
    
    <!-- Title Bar -->
    <rect x="8" y="8" width="{width-16}" height="24" fill="#00fbfb"/>
    <text x="16" y="24" fill="#002020" font-size="12" class="font-mono font-bold">C:\\SYSTEM32\\BOOT.EXE - whoami</text>
    
    <!-- Close Button -->
    {draw_retro_bevel(width-32, 12, 16, 16, "#20201f", False, 1)}
    <path d="M {width-28} 16 L {width-20} 24 M {width-20} 16 L {width-28} 24" stroke="#e5e2e1" stroke-width="1.5" />
    <!-- Min/Max Buttons -->
    {draw_retro_bevel(width-52, 12, 16, 16, "#20201f", False, 1)}
    {draw_retro_bevel(width-72, 12, 16, 16, "#20201f", False, 1)}
    
    <!-- Inner Area -->
    {draw_retro_bevel(8, 36, width-16, height-44, "#0e0e0e", True, 2)}
    
    <!-- Terminal Text -->
    <text x="32" y="72" fill="#b9cac9" font-size="14" class="font-mono">BIOS Date 09/24/95 14:23:01 Ver 1.00</text>
    <text x="32" y="92" fill="#b9cac9" font-size="14" class="font-mono">CPU: Intel(R) Neural Coprocessor</text>
    
    <text x="32" y="132" fill="#00dddd" font-size="14" class="font-mono">C:\\&gt; EXEC_PROFILE.BAT</text>
    
    <text x="32" y="162" fill="#b9cac9" font-size="14" class="font-mono">&gt; INITIALIZING PROFILE DATABANKS...</text>
    <text x="32" y="192" fill="#ffffff" font-size="14" class="font-mono" font-weight="bold">&gt; IDENTITY: Saanvi Sharma</text>
    <text x="32" y="222" fill="#ffabf3" font-size="14" class="font-mono">&gt; ROLE: AI Engineer / Systems Architect</text>
    <text x="32" y="252" fill="#ffffff" font-size="14" class="font-mono">&gt; MISSION: Building adaptive AI systems that scale gracefully.</text>
    <text x="32" y="282" fill="#00dddd" font-size="14" class="font-mono">&gt; STATUS: Ready for input.</text>
    
    <text x="32" y="322" fill="#00dddd" font-size="14" class="font-mono">C:\\&gt; <tspan class="pulse">_</tspan></text>
    
    <!-- Avatar Section -->
    <g transform="translate(560, 50)">
        {draw_retro_bevel(0, 0, 190, 240, "#20201f", False, 2)}
        <image x="4" y="4" width="182" height="232" href="{avatar_b64}" preserveAspectRatio="xMidYMid slice" filter="grayscale(100%) contrast(1.5)" />
        {draw_retro_bevel(120, 220, 75, 24, "#ffabf3", False, 1)}
        <text x="132" y="236" fill="#5b005b" font-size="10" class="font-mono font-bold pulse">ONLINE</text>
    </g>
    
    <!-- Watermark -->
    <text x="450" y="320" fill="#353535" font-size="90" font-weight="900" opacity="0.2" class="font-sans">AI_ENG</text>
    '''
    
    with open('assets/hero.svg', 'w', encoding='utf-8') as f:
        f.write(wrap_svg(width, height, content))

def generate_modules():
    print("Generating modules.svg...")
    width = 380
    height = 420
    
    content = f'''
    <!-- Outer Window -->
    {draw_retro_bevel(0, 0, width, height, "#20201f", False, 2)}
    
    <!-- Title Bar -->
    <rect x="8" y="8" width="{width-16}" height="24" fill="#ffd7f5"/>
    <text x="16" y="24" fill="#380038" font-size="12" class="font-mono font-bold">LOADED_MODULES.SYS</text>
    
    <!-- Inner Area -->
    {draw_retro_bevel(8, 36, width-16, height-44, "#0e0e0e", True, 2)}
    
    <g transform="translate(24, 56)">
        <text x="0" y="10" fill="#b9cac9" font-size="10" class="font-mono">CORE_ENGINES</text>
        <line x1="0" y1="16" x2="332" y2="16" stroke="#3a4a49" stroke-width="1"/>
        
        {draw_retro_bevel(0, 26, 95, 24, "#131313", False, 1)}
        <text x="8" y="42" fill="#00dddd" font-size="12" class="font-mono">Python_3.x</text>
        
        {draw_retro_bevel(105, 26, 80, 24, "#131313", False, 1)}
        <text x="113" y="42" fill="#00dddd" font-size="12" class="font-mono">Rust_1.7</text>
        
        {draw_retro_bevel(195, 26, 50, 24, "#131313", False, 1)}
        <text x="203" y="42" fill="#00dddd" font-size="12" class="font-mono">C++</text>
    </g>
    
    <g transform="translate(24, 146)">
        <text x="0" y="10" fill="#b9cac9" font-size="10" class="font-mono">NEURAL_NETS</text>
        <line x1="0" y1="16" x2="332" y2="16" stroke="#3a4a49" stroke-width="1"/>
        
        {draw_retro_bevel(0, 26, 75, 24, "#ffabf3", False, 1)}
        <text x="8" y="42" fill="#5b005b" font-size="12" class="font-mono font-bold">PyTorch</text>
        
        {draw_retro_bevel(85, 26, 95, 24, "#131313", False, 1)}
        <text x="93" y="42" fill="#ffd7f5" font-size="12" class="font-mono">TensorFlow</text>
        
        {draw_retro_bevel(190, 26, 60, 24, "#131313", False, 1)}
        <text x="198" y="42" fill="#ffd7f5" font-size="12" class="font-mono">Keras</text>
    </g>
    
    <g transform="translate(24, 236)">
        <text x="0" y="10" fill="#b9cac9" font-size="10" class="font-mono">DATABASES</text>
        <line x1="0" y1="16" x2="332" y2="16" stroke="#3a4a49" stroke-width="1"/>
        
        {draw_retro_bevel(0, 26, 95, 24, "#131313", False, 1)}
        <text x="8" y="42" fill="#00fbfb" font-size="12" class="font-mono">PostgreSQL</text>
        
        {draw_retro_bevel(105, 26, 80, 24, "#131313", False, 1)}
        <text x="113" y="42" fill="#00fbfb" font-size="12" class="font-mono">Pinecone</text>
        
        {draw_retro_bevel(195, 26, 60, 24, "#131313", False, 1)}
        <text x="203" y="42" fill="#00fbfb" font-size="12" class="font-mono">Redis</text>
    </g>
    '''
    with open('assets/modules.svg', 'w', encoding='utf-8') as f:
        f.write(wrap_svg(width, height, content))


def generate_missions():
    print("Generating missions.svg...")
    width = 400
    height = 420
    
    mission1_img = "https://lh3.googleusercontent.com/aida-public/AB6AXuC2sjvwcyO6_xPWoPBqXptd4B50aLv8MVt0n2hj-WvecZG1Yc2dsdAoQUf17lWns1xabVeYjyay11ZnVClTeLia2OdFdiUDKGMvrvzd5dUc-61V0P7nP_Y4w9JHjq2auzUZG0zaF_EQunmPyUIh-jjqUXZHL-01felXcxRrjmu009BR2knxhf1qDiS8J-7X_wOQGfTa6gHCzXe-1Mfk6Q_KXXtbSc70_EMw9jFy7ULxCKYMyaLzU2FLZHYAmoABw7rk8A"
    m1_b64 = fetch_image_as_base64(mission1_img)
    
    content = f'''
    <!-- Outer Window -->
    {draw_retro_bevel(0, 0, width, height, "#20201f", False, 2)}
    
    <!-- Title Bar -->
    <rect x="8" y="8" width="{width-16}" height="24" fill="#ffffff"/>
    <text x="16" y="24" fill="#003737" font-size="12" class="font-mono font-bold">ACTIVE_MISSIONS.DIR</text>
    <rect x="{width-68}" y="10" width="56" height="20" fill="#0e0e0e"/>
    <text x="{width-60}" y="24" fill="#ffffff" font-size="10" class="font-mono font-bold">2 FILES</text>
    
    <!-- Inner Area -->
    {draw_retro_bevel(8, 36, width-16, height-44, "#0e0e0e", True, 2)}
    
    <!-- Mission 1 -->
    <g transform="translate(16, 44)">
        {draw_retro_bevel(0, 0, 368, 170, "#131313", False, 2)}
        {draw_retro_bevel(8, 8, 352, 80, "#0e0e0e", True, 2)}
        <image x="10" y="10" width="348" height="76" href="{m1_b64}" preserveAspectRatio="xMidYMid slice" filter="grayscale(100%)" />
        <text x="8" y="108" fill="#ffffff" font-size="14" class="font-mono font-bold">&gt; Cascade GenAI Study</text>
        <text x="8" y="128" fill="#b9cac9" font-size="12" class="font-mono">An adaptive LLM-based study companion that dynamically</text>
        <text x="8" y="142" fill="#b9cac9" font-size="12" class="font-mono">adjusts difficulty based on real-time neural metrics.</text>
        
        <rect x="8" y="152" width="40" height="14" fill="#2a2a2a" stroke="#3a4a49"/>
        <text x="12" y="162" fill="#00fbfb" font-size="10" class="font-mono">LLM</text>
        
        <rect x="52" y="152" width="60" height="14" fill="#2a2a2a" stroke="#3a4a49"/>
        <text x="56" y="162" fill="#00fbfb" font-size="10" class="font-mono">ADAPTIVE</text>
    </g>
    
    <!-- Mission 2 -->
    <g transform="translate(16, 230)">
        {draw_retro_bevel(0, 0, 368, 170, "#131313", False, 2)}
        {draw_retro_bevel(8, 8, 352, 80, "#2a2a2a", True, 2)}
        <!-- Vector DB Icon -->
        <circle cx="184" cy="48" r="24" fill="#00dddd" opacity="0.1"/>
        <text x="172" y="58" fill="#00dddd" font-size="28" font-family="sans-serif">&#8862;</text>
        
        <text x="8" y="108" fill="#ffffff" font-size="14" class="font-mono font-bold">&gt; Auto-Prescription Core</text>
        <text x="8" y="128" fill="#b9cac9" font-size="12" class="font-mono">High-reliability diagnostic clustering system.</text>
        <text x="8" y="142" fill="#b9cac9" font-size="12" class="font-mono">Cross-references symptoms with vector search.</text>
        
        <rect x="8" y="152" width="70" height="14" fill="#2a2a2a" stroke="#3a4a49"/>
        <text x="12" y="162" fill="#ffabf3" font-size="10" class="font-mono">VECTOR_DB</text>
        
        <rect x="82" y="152" width="80" height="14" fill="#2a2a2a" stroke="#3a4a49"/>
        <text x="86" y="162" fill="#ffabf3" font-size="10" class="font-mono">HEALTH-TECH</text>
    </g>
    '''
    with open('assets/missions.svg', 'w', encoding='utf-8') as f:
        f.write(wrap_svg(width, height, content))

def generate_status():
    print("Generating status.svg...")
    width = 800
    height = 120
    
    content = f'''
    <!-- Outer Window -->
    {draw_retro_bevel(0, 0, width, height, "#20201f", False, 2)}
    
    <!-- Title Bar -->
    <rect x="8" y="8" width="{width-16}" height="24" fill="#353535"/>
    <text x="16" y="24" fill="#e5e2e1" font-size="12" class="font-mono font-bold">SYS.STATUS // DIAGNOSTICS</text>
    
    <!-- Inner Area -->
    {draw_retro_bevel(8, 36, width-16, height-76, "#0e0e0e", True, 2)}
    
    <!-- Bar 1 -->
    <g transform="translate(24, 52)">
        <text x="0" y="12" fill="#b9cac9" font-size="12" class="font-mono">MEM.COFFEE_LEVEL</text>
        <text x="210" y="12" fill="#00dddd" font-size="12" class="font-mono" text-anchor="end">88%</text>
        {draw_retro_bevel(0, 20, 210, 16, "#20201f", True, 1)}
        <rect x="2" y="22" width="182" height="12" fill="#00dddd" opacity="0.8"/>
    </g>
    
    <!-- Bar 2 -->
    <g transform="translate(290, 52)">
        <text x="0" y="12" fill="#b9cac9" font-size="12" class="font-mono">BUGS_CRUSHED.LOG</text>
        <text x="210" y="12" fill="#ffabf3" font-size="12" class="font-mono" text-anchor="end">1,402</text>
        {draw_retro_bevel(0, 20, 210, 16, "#20201f", True, 1)}
        <rect x="2" y="22" width="206" height="12" fill="#ffabf3" opacity="0.8"/>
    </g>
    
    <!-- Bar 3 -->
    <g transform="translate(560, 52)">
        <text x="0" y="12" fill="#b9cac9" font-size="12" class="font-mono">FOCUS_MODE</text>
        <text x="210" y="12" fill="#00fbfb" font-size="12" class="font-mono font-bold pulse" text-anchor="end">ENGAGED</text>
        {draw_retro_bevel(0, 20, 210, 16, "#20201f", True, 1)}
        <rect x="2" y="22" width="195" height="12" fill="#00fbfb" opacity="0.8"/>
    </g>
    '''
    with open('assets/status.svg', 'w', encoding='utf-8') as f:
        f.write(wrap_svg(width, height, content))

if __name__ == "__main__":
    generate_hero()
    generate_modules()
    generate_missions()
    generate_status()
    print("Done generating SVGs.")
