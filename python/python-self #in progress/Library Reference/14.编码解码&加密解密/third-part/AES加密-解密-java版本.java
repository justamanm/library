import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Base64.Decoder;
import java.util.Base64.Encoder;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.X509EncodedKeySpec;

import java.util.Base64;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;


public class Banshi {
    public static void main(String[] args) throws Exception {
        String encryptText = encrypt("123456abcd", "1234567812345678");
        System.out.println(encryptText);
        String originText = decrypt(encryptText);
        System.out.println(originText);
    }
//    加密
//    str：原文，密钥 key: "1234567812345678"
//    PKCS5Padding指定如果被加密数据不足16位，补位方式
//    iv加强加密
    public static String encrypt(String str, String key) throws Exception {
        String iv= "jszwfwhanweb2016";
//        实例化SecretKeySpec类,根据字节数组来构造SecretKeySpec
        Key secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
//        实例化IvParameterSpec对象，使用指定的初始化向量
        IvParameterSpec ivspec = new IvParameterSpec(iv.getBytes());
//        创建密码器
        Cipher instance = Cipher.getInstance("AES/CBC/PKCS5Padding");
//        初始化密码器对象
        instance.init(1, secretKeySpec, ivspec);
//        执行加密操作
        byte[] ret = instance.doFinal(str.getBytes());
//        加密后的数据
        String encodedText = Base64.getEncoder().encodeToString(ret);
        return encodedText;
    }

//  解密01-有加强加密
    public static String decrypt(String encryptedData) throws Exception {
        String key = "1234567812345678";
        String iv= "jszwfwhanweb2016";
        byte[] ciphertext = Base64.getDecoder().decode(encryptedData);
        try {
            SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
            IvParameterSpec ivspec = new IvParameterSpec(iv.getBytes());
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, ivspec);

            byte[] ret = cipher.doFinal(ciphertext);
            String plaintext = new String(ret,"UTF-8").trim();
            return plaintext;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

//  解密02-无加强加密
    public static String decrypt_1(String encryptedData) throws Exception {
        String key = "1234567812345678";

        try {
            Key secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
            Cipher instance = Cipher.getInstance("AES/CBC/PKCS5Padding");
            instance.init(2, secretKeySpec);
            try {
                return new String(instance.doFinal(to_bytes(encryptedData)), "utf-8");
            } catch (Exception e) {
                return null;
            }
        } catch (Exception e2) {
            return null;
        }
    }

//  将要解密的字符串做特殊处理转换为字节数组
    public static byte[] to_bytes(String str) {
        if (str == null) {
            return null;
        }
        int length = str.length();
        if (length % 2 == 1) {
            return null;
        }
        byte[] bArr = new byte[(length / 2)];
        for (int i = 0; i != length / 2; i++) {
            bArr[i] = (byte) Integer.parseInt(str.substring(i * 2, (i * 2) + 2), 16);
        }
        return bArr;
    }

}


