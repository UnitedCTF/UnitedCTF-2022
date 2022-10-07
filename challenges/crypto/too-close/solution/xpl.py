#!/usr/bin/python3
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
import gmpy

e = 0x10001
n = 0x96B581AED615E5499976A5D6921FD8135F8BF7BE296CDF311FB752484C3350A390FA354F1457BF32940CC0315628A57689BC1C12039C7E63F42A1E1BCE2359EED540D9C3421BF69E268CC38E17DB680B045017B9E65F15D46CA41CFF2497F2833F63B159AC99AB9FB2706D440D36930B311DC76748D8B05C042BABDED675F3570A613DB006C5B057A0A56EAB473D432C9ADE7741313938E8283B48E996A2C96D7463BD64D4A330B6AC37F15C97F1C83A1F78C2540DE9C83221ABD2D77C1FDD6C17B717BDFC2670F9C465137E777014501B3B4A57D3C65A8A6B304FE4BEC8495B33D375751F3B27BA853686B6255ADEB17CC02FB110E2A73EF8963A56AA8FBEB1C331A19134332147647F0409C4BCD11BA3D29B189040CCC770AE4B71A97F49F80438C0E915C77D9F8D2014EE27455257C8ACA6BC254B9B71DA5EB4C2971342CDFA83D1B8A03823ABE1DB3E0ED27819304476B4838A249CCAC5003C4A8D3EA895CFE52D3C10AB11D9073FA819E816582BAD29C9CB69466BAF069B56EC500F799B6070CC9E8BC8C1D527B80D8A4F83B7AEAEBC146CCFB09040413E4357E261E33C153267E2BD4F7F84871A47251BC7655B1473408B8D80BDEBB6D9D7D7652974AFAEE79E5075CA2FBF40E7B5491F7E6FF7EC5887ECC90377E4E79824AF8F449BECE4670DFAB175C564BB094E14996920BC1CF339B355B96AD935D9CA77C78F4297
ciphertext = 0x93279830576C7290458B2B15F908D0DDAB99D36DA62C02744145F124223F748722B49DF2914445FD10A0B58A64D7EC84445D7DF9DE5EEA7AE1BB24FC87A51112DD35441688C253F4B44DF0CEA7E659DC5B73242A1D7AAA8EBF9EB5D22251D9C07AFBD7A77F780D9CA702F5BBDBAAD9958718AA5658931FC738B48ABA963D3312ACB0B4220476A05F2FC6F8345A5BC4FC3E8516D78DC52FE876D5E2593B194B21D9B6506B915FA51486CB04874E612FDCD893F9066CBE23C0436B1FC589E007BB5BCC1FA3C4DAD53A037030AE2C2445E88290641021EDB41C8C5FB6875379227F3117D96B830349A0BF297B6A89BA78BA3B8A7F9D141BE21F9B38C720FC2164267EC8770C03940FF414FF7E76251DF06EF2225CCE4CA939381EBECF61C1FF022ED85ED79D78F921A42CEC641C6721B9D81A9AB676A0FCBFE09E17079D8DE28C6D0D8B9BE94BA49234227C0FE2B82297AFFA9EF8FE9480B750A55A79FD181D4DD0807356255A7DBCA571F626670E588E5705CDF2A479BD12B486D97B9D3FB0D5949653BE00CEF05C5B973F2ED161DC6E79B76F9A26A96EE6D45C210E407C317CCDBF9EE3E7C76D783082503CDCEEB8F3414990D22A454C7BCFA3EE3435E031B525A8178DBCB1645D01AD227C4FA603B5D27734AF2733A53DB9402966FA306F4FB84FB9B7CB6638FAAA0360FE21DA900AA7FB3AE537F2FC417882F40924EDCDD110

n_sqrt = gmpy.sqrt(n)
p = gmpy.next_prime(n_sqrt)
q = n // p
phi = (p - 1) * (q - 1)
d = gmpy.invert(e, phi)

plaintext = pow(ciphertext, d, n)
flag = l2b(plaintext).decode()

print(flag)