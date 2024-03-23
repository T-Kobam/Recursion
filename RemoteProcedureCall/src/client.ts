import * as net from "net";
import * as Log4js from "log4js";

const PORT: number = 50000;
const HOST: string = "localhost"

/**
 * request用のインターフェース
 */
interface Request {
    method: string,
    params: number[] | string[],
    param_types: string[],
    id: string   
}

// 設定ファイルの読み込み
Log4js.configure("./config/development.json");

// ロガーの設定
const logger: Log4js.Logger = Log4js.getLogger("access");
// ソケットの作成
const client: net.Socket = new net.Socket();

const req: Request = {
    method: "reverse",
    params: ["abcdef"],
    param_types: ["string"],
    id: "1"
}
// サーバに接続
client.connect(PORT, HOST, () => {
    logger.info("Connect started");
    // JSON文字列に変換しメッセージを送信
    client.write(JSON.stringify(req));
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

