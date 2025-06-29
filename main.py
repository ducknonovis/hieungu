import discord
from discord.ext import commands
import asyncio
from flask import Flask
import threading
import os

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

# Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot online!'

# Discord bot command
@bot.command()
async def nukehieu(ctx):
    message = """# hiếu đang đòi báo lên an ninh mạng kìa
## em sợ quá em xin phép truy cứu hình sự anh hiếu:
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
VĂN BẢN TRUY TỐ HÌNH SỰ

Số: … /2025/TTHS

V/v: Truy tố hình sự đối với Nguyễn Mạnh Hiếu

Kính gửi:

Viện kiểm sát nhân dân …

Cơ quan Cảnh sát điều tra …

Căn cứ vào kết quả điều tra bước đầu và các chứng cứ đã thu thập được, chúng tôi xác định:

I. Thông tin đối tượng:

Họ tên: Nguyễn Mạnh Hiếu

Ngày sinh: … / … / 2011 (14 tuổi)

Địa chỉ thường trú: …

Nghề nghiệp / Học sinh lớp: …

II. Hành vi phạm tội:
Vào khoảng tháng … năm 2025, Nguyễn Mạnh Hiếu đã:

Sử dụng công cụ tấn công từ chối dịch vụ (DDoS) để gây gián đoạn, làm tê liệt hệ thống máy chủ của các tổ chức, cá nhân.

Tự phát triển và chia sẻ phần mềm Trojan, với mục đích lén xâm nhập, thu thập thông tin, kiểm soát trái phép thiết bị của người khác, từ đó gây nguy hiểm cho an ninh mạng.

Theo các điều khoản quy định tại:

Điều 287 Bộ luật Hình sự 2015 (sửa đổi, bổ sung 2017) về tội đưa hoặc sử dụng trái phép thông tin mạng máy tính, mạng viễn thông.

Điều 289 Bộ luật Hình sự 2015 về tội cản trở hoặc gây rối loạn hoạt động của mạng máy tính, mạng viễn thông, phương tiện điện tử.

Hành vi của Nguyễn Mạnh Hiếu đã đủ yếu tố cấu thành tội phạm, gây thiệt hại và nguy hiểm cho xã hội.

III. Đề nghị:

Truy cứu trách nhiệm hình sự đối với Nguyễn Mạnh Hiếu theo quy định pháp luật.

Áp dụng biện pháp xử lý đối với người chưa đủ 16 tuổi phạm tội theo Điều 91, Điều 92 Bộ luật Hình sự 2015 (về nguyên tắc xử lý đối với người dưới 18 tuổi).

Tiếp tục điều tra mở rộng để xác định đồng phạm, nguồn gốc công cụ phạm tội và các thiệt hại thực tế.

ddos trojan cái lồn mày hiếu ạ hsg tỉnh cũng chỉ là thằng trẻ con rách bú mẹ dái tao đi 
<@929981636404199465>"""
    
    while True:
        try:
            # Check if proof.png exists, otherwise send without attachment
            image_path = "proof.png"
            if os.path.exists(image_path):
                await ctx.send(message, file=discord.File(image_path))
            else:
                await ctx.send(message)
            await asyncio.sleep(1)  # Wait for 1 second
        except Exception as e:
            print(f"Error: {e}")
            break

# Run Flask app in a separate thread
def run_flask():
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

# Bot event: on ready
@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

# Start Flask and Discord bot
if __name__ == "__main__":
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start Discord bot using environment variable
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: DISCORD_TOKEN environment variable not set.")
        exit(1)
    bot.run(token)
