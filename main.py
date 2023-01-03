int factorielle(int n) {
    if (n < 2) {
        return 1;
    }
    else {
        return n * factorielle(n - 1);
    }
}
