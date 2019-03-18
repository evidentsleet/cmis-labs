using System;

namespace Lab1
{
    class Crypter
    {
        int width;
        int height;
        int[] permutation;

        public Crypter(int len, string keyword)
        {
            width = keyword.Length;
            height = len / keyword.Length;
            permutation = new int[keyword.Length];
            for (int i = 0; i < permutation.Length; i++)
                permutation[i] = i;
            Array.Sort(keyword.ToCharArray(), permutation);
        }

        public string Encode(string src)
        {
            char[] res = new char[src.Length];
            for (int i = 0; i < height; i++)
                for (int j = 0; j < width; j++)
                    res[i * width + j] = src[permutation[j] * height + i];
            return new string(res);

        }
        public string Decode(string src)
        {
            char[] res = new char[src.Length];
            for (int i = 0; i < width; i++)
                for (int j = 0; j < height; j++)
                    res[permutation[i] * height + j] = src[j * width + i];
            return new string(res);
        }
    }

    class MainClass
    {
        public static void Main(string[] args)
        {
            do
            {
                Console.WriteLine("(1)Зашифровать или (2)расшифровать сообщение?");
                string choice = Console.ReadLine();
                Console.WriteLine("Введите сообщение: ");
                string str = Console.ReadLine().ToLower();
                Console.WriteLine(str.Length);
                Console.WriteLine("Введите ключ: ");
                string key = Console.ReadLine().ToLower();

                Crypter crypter = new Crypter(str.Length, key);
                if (choice == "1")
                {
                    string crypted = crypter.Encode(str);
                    Console.WriteLine($"Зашифрованный текст: {crypted}");
                }
                else
                {
                    string encrypted = crypter.Decode(str);
                    Console.WriteLine($"Расшифрованный текст: {encrypted}");
                }
                Console.WriteLine("Продолжить работу? да/нет");
                if (Console.ReadLine() == "нет") break;
            }
            while (true);
        }
    }
}