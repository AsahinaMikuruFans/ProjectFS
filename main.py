# _*_ coding: utf-8 _*_


def main():
    from source.core.const.Const import gl_WindowWidth, gl_WindowHeight, gl_nextLevelWindowWidth, \
        gl_nextLevelWindowHeight
    from gameApp import gameApp

    game = gameApp("FinalSound终曲", gl_nextLevelWindowWidth, gl_nextLevelWindowHeight, False, 0, 32)
    game.MainLoop()


if __name__ == "__main__":
    main()
