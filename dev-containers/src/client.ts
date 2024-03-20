import * as net from "net";
import * as Config from "config";
import * as Path from "path";
import * as Log4js from "log4js";

const PORT: number = 50000;
const HOST: string = "localhost"

// 設定ファイルの読み込み
// const configure = Config.util.loadFileConfigs(Path.join(__dirname, "config")).log4js;
Log4js.configure("./config/development.json");

// ロガーの設定
const logger: Log4js.Logger = Log4js.getLogger("access");
// ソケットの作成
const client: net.Socket = new net.Socket();

// サーバに接続
client.connect(PORT, HOST, () => {
    logger.info("Connect started");
    // メッセージの送信
    client.write("test message");
});

// サーバからのデータを受信する
client.on("data", (data: Buffer) => {
    logger.info("Recived data: " + data);
    // 接続を破棄
    client.destroy();
});

// 接続破棄時の処理
client.on("close", () => {
    logger.info("Connection closed");
});

// エラー処理
client.on("error", (err: Error) => {
    logger.warn("Error: ", err);
});