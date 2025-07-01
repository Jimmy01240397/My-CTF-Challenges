#include <emscripten.h>
#include <emscripten/html5.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>

EMSCRIPTEN_KEEPALIVE
static inline uint64_t rotl64(uint64_t x, unsigned s)
{
    return (x << s) | (x >> (64U - s));
}

EMSCRIPTEN_KEEPALIVE
int flagchecker(const char *flag)
{
    const uint32_t KEY = 0xfd9ea72dU;
    const uint64_t ANS[5] = {
        0x69282a668aef666aULL, 0x633525f4d7372337ULL,
        0x9db9a5a0dcc5dd7dULL, 0x9833afafb8381a2fULL,
        0x6fac8c8726464726ULL
    };

    if (!flag || strlen(flag) != 40) return 0;
    uint64_t* data = (uint64_t*)flag;

    for (int i = 0; i < 5; ++i) {
        uint64_t chunk = data[i];
        unsigned s = (KEY >> (i * 6)) & 0b111111;
        if (rotl64(chunk, s) != ANS[i]) return 0;
    }
    return 1;
}

EMSCRIPTEN_KEEPALIVE
EM_BOOL on_check(int evType, const EmscriptenMouseEvent *e, void *user)
{
    (void)e; (void)user;

    char buf[64] = {0};
    EM_ASM({
        const val  = document.getElementById('flagInput').value;
        stringToUTF8(val, $0, 64);
    }, buf);

    int ok = flagchecker(buf);
    EM_ASM({
        document.getElementById('result').textContent = $0 ? 'Success' : 'Wrong flag';
    }, ok);

    return EM_TRUE;
}

EMSCRIPTEN_KEEPALIVE
int main(void)
{
    emscripten_set_click_callback("#checkBtn", NULL, EM_TRUE, on_check);
    return 0;
}
