{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "n, m = map(int, sys.stdin.readline().rstrip().split())\n",
    "dic={}\n",
    "arr=[]\n",
    "result = 0\n",
    "for i in range(n):\n",
    "    a = str(sys.stdin.readline().rstrip())\n",
    "    dic[a] = 0\n",
    "for i in range(m):\n",
    "    a = str(sys.stdin.readline().rstrip())\n",
    "    if a in dic:\n",
    "        result += 1\n",
    "        arr.append(a)\n",
    "arr.sort()\n",
    "print(result)\n",
    "for i in arr:\n",
    "    print(i)"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
