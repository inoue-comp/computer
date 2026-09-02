using System.Linq;
using Raylib_cs;

namespace _3DGame
{
    public static class FontHelper
    {
        /// <summary>
        /// 指定した文字列に含まれる文字だけを厳選し、Raylib用日本語フォントをロードします。
        /// </summary>
        public static Font LoadJapaneseFont(string fontPath, int fontSize, string usedText)
        {
            // 重複文字の除去
            string uniqueChars = new string(usedText.Distinct().ToArray());

            // Unicodeコードポイント列の作成
            int[] codepoints = uniqueChars.Select(c => char.ConvertToUtf32(c.ToString(), 0)).ToArray();

            // フォントのロード
            return Raylib.LoadFontEx(fontPath, fontSize, codepoints, codepoints.Length);
        }
    }
}