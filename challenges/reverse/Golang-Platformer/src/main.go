// credits : https://github.com/faiface/pixel-examples/tree/master/platformer
package main

import (
	"bufio"
	"encoding/base64"
	"flag"
	"fmt"
	"image"
	"image/color"
	"io"
	"log"
	"math"
	"math/rand"
	"os"
	"runtime"
	"strings"
	"time"

	_ "image/png"

	"github.com/faiface/pixel"
	"github.com/faiface/pixel/imdraw"
	"github.com/faiface/pixel/pixelgl"
	"golang.org/x/image/colornames"
)

const imgF = "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"
const imgG = "iVBORw0KGgoAAAANSUhEUgAAAA4AAAAMCAYAAABSgIzaAAAAnklEQVQoU2NkQALfV1f+R+aD2Jyh7Yz/69X/MzbeRKXRNXJ+z2f4zjmRAU4TqxGXjejijP8/MYCdd+GyEVzOQPccBh8s2avOAHIyiDmUNNa3PQb7sbFKFu5HoL8ZGPkQwQFUA+Y0/HRB+BGuUYYVPeDg/PonvzE1wmUXvcCIfLhcnAQ4JGEJARyqWDWCFCIbhE8jyDSYIbDkhcxHtxEA3+qG+ZAYmn4AAAAASUVORK5CYII="
const imgW = "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"

func DecodeBase64(data string) io.Reader {
	return base64.NewDecoder(base64.StdEncoding, strings.NewReader(data))
}

func loadPicture(b64img string) (picture pixel.Picture, anim pixel.Rect, err error) {

	pictureImg, _, err := image.Decode(DecodeBase64(b64img))

	if err != nil {
		return nil, pixel.Rect{}, err
	}

	picture = pixel.PictureDataFromImage(pictureImg)
	frame := pixel.R(0, 0, picture.Bounds().W(), picture.Bounds().H())

	return picture, frame, nil
}

type platform struct {
	rect  pixel.Rect
	color color.Color
}

func (p *platform) draw(imd *imdraw.IMDraw) {
	imd.Color = p.color
	imd.Push(p.rect.Min, p.rect.Max)
	imd.Rectangle(0)
}

type Phys struct {
	gravity   float64
	runSpeed  float64
	jumpSpeed float64

	rect   pixel.Rect
	vel    pixel.Vec
	ground bool
}

func (playerPhys *Phys) update(dt float64, ctrl pixel.Vec, platforms []platform, gol goal) bool {
	won := false

	// apply controls
	switch {
	case ctrl.X < 0:
		playerPhys.vel.X = -playerPhys.runSpeed
	case ctrl.X > 0:
		playerPhys.vel.X = +playerPhys.runSpeed
	default:
		playerPhys.vel.X = 0
	}

	// apply gravity and velocity
	playerPhys.vel.Y += playerPhys.gravity * dt
	playerPhys.rect = playerPhys.rect.Moved(playerPhys.vel.Scaled(dt))

	// check collisions against each platform
	playerPhys.ground = false

	if playerPhys.vel.Y <= 0 {

		for _, p := range platforms {

			if playerPhys.rect.Max.X <= p.rect.Min.X || playerPhys.rect.Min.X >= p.rect.Max.X {
				continue
			}

			if playerPhys.rect.Min.Y > p.rect.Max.Y || playerPhys.rect.Min.Y < p.rect.Max.Y+playerPhys.vel.Y*dt {
				continue
			}

			playerPhys.vel.Y = 0
			playerPhys.rect = playerPhys.rect.Moved(pixel.V(0, p.rect.Max.Y-playerPhys.rect.Min.Y))
			playerPhys.ground = true
		}
	}

	// jump if on the ground and the player wants to jump
	if playerPhys.ground && ctrl.Y > 0 {
		playerPhys.vel.Y = playerPhys.jumpSpeed
	}

	// Restart if fell below -40
	if playerPhys.rect.Min.Y < -100 {
		playerPhys.rect = playerPhys.rect.Moved(playerPhys.rect.Center().Scaled(-1))
		playerPhys.vel = pixel.ZV
	}

	if playerPhys.rect.Min.Y > gol.pos.Y-gol.radius && playerPhys.rect.Min.X > gol.pos.X-gol.radius {
		won = true
	}
	return won
}

type Anim struct {
	picture pixel.Picture
	anim    pixel.Rect
	sprite  *pixel.Sprite
}

func (playerAnim *Anim) draw(t pixel.Target, rect pixel.Rect) {

	if playerAnim.sprite == nil {
		playerAnim.sprite = pixel.NewSprite(nil, pixel.Rect{})
	}

	playerAnim.sprite.Set(playerAnim.picture, playerAnim.picture.Bounds())
	playerAnim.sprite.Draw(t, pixel.IM.
		ScaledXY(pixel.ZV, pixel.V(
			rect.W()/playerAnim.sprite.Frame().W(),
			rect.H()/playerAnim.sprite.Frame().H(),
		)).
		Moved(rect.Center()),
	)
}

type goal struct {
	pos    pixel.Vec
	radius float64
	step   float64

	counter float64
	cols    [5]pixel.RGBA
}

func (g *goal) update(dt float64) {
	g.counter += dt

	for g.counter > g.step {
		g.counter -= g.step

		for i := len(g.cols) - 2; i >= 0; i-- {
			g.cols[i+1] = g.cols[i]
		}
		g.cols[0] = randomNiceColor()
	}
}

func (g *goal) draw(imd *imdraw.IMDraw) {

	for i := len(g.cols) - 1; i >= 0; i-- {
		imd.Color = g.cols[i]
		imd.Push(g.pos)
		imd.Circle(float64(i+1)*g.radius/float64(len(g.cols)), 0)
	}
}

func randomNiceColor() pixel.RGBA {
again:
	r := rand.Float64()
	g := rand.Float64()
	b := rand.Float64()
	len := math.Sqrt(r*r + g*g + b*b)

	if len == 0 {
		goto again
	}
	return pixel.RGB(r/len, g/len, b/len)
}

func run() {
	won := false
	rand.Seed(time.Now().UnixNano())

	runSpeedMultiplier := flag.Float64("runSpeedMultiplier", 1, "Your speed will be multiplied by this factor")
	flag.Parse()

	playerPicture, PlayerAnim, err := loadPicture(imgG)

	if err != nil {
		panic(err)
	}
	flagPicture, flagAnim, err := loadPicture(imgF)

	if err != nil {
		panic(err)
	}
	winPicture, winAnim, err := loadPicture(imgW)

	if err != nil {
		panic(err)
	}

	// Window initialization
	cfg := pixelgl.WindowConfig{
		Title:  "Platformer",
		Bounds: pixel.R(0, 0, 1024, 768),
		VSync:  true,
	}
	win, err := pixelgl.NewWindow(cfg)
	if err != nil {
		panic(err)
	}

	playerPhys := &Phys{
		gravity:   -512,
		runSpeed:  64 * *runSpeedMultiplier,
		jumpSpeed: 192,
		rect:      pixel.R(-7, -6, 7, 6),
	}
	flagPhys := pixel.R(-320, -15, -95, 35)
	winPhys := pixel.R(420, 45, 545, 170)

	flagPic := &Anim{
		picture: flagPicture,
		anim:    flagAnim,
	}
	winPic := &Anim{
		picture: winPicture,
		anim:    winAnim,
	}
	playerPic := &Anim{
		picture: playerPicture,
		anim:    PlayerAnim,
	}

	// hardcoded level
	platforms := []platform{
		{rect: pixel.R(-500, -20, 50, -17)},
		{rect: pixel.R(50, 13, 110, 16)},
		{rect: pixel.R(160, -20, 190, -17)},
		{rect: pixel.R(190, 13, 240, 16)},
		{rect: pixel.R(240, 46, 290, 49)},
		{rect: pixel.R(330, 35, 400, 38)},
		{rect: pixel.R(400, 68, 460, 71)},
		{rect: pixel.R(460, 100, 530, 103)},
	}

	for i := range platforms {
		platforms[i].color = randomNiceColor()
	}

	gol := &goal{
		pos:    pixel.V(495, 120),
		radius: 18,
		step:   1.0 / 7,
	}

	canvas := pixelgl.NewCanvas(pixel.R(-160/2, -120/2, 160/2, 120/2))
	imdFlag := imdraw.New(flagPicture)
	imdPlayer := imdraw.New(playerPicture)
	imdWin := imdraw.New(winPicture)

	camPos := pixel.ZV

	last := time.Now()
	pause := false

	for !win.Closed() {
		var dt float64

		if !pause {
			dt = time.Since(last).Seconds()
		}

		last = time.Now()

		// lerp the camera position towards the gopher
		camPos = pixel.Lerp(camPos, playerPhys.rect.Center(), 1-math.Pow(1.0/128, dt))
		cam := pixel.IM.Moved(camPos.Scaled(-1))
		canvas.SetMatrix(cam)

		// slow motion with tab
		if win.Pressed(pixelgl.KeyTab) {
			dt /= 8
		}

		// Pause with space
		if win.JustPressed(pixelgl.KeySpace) {
			if pause {
				pause = false
			} else {
				pause = true
			}
		}

		// Game stop when won
		if won {
			dt = 0
		}

		// restart the level on pressing enter
		if win.JustPressed(pixelgl.KeyEnter) {
			playerPhys.rect = playerPhys.rect.Moved(playerPhys.rect.Center().Scaled(-1))
			playerPhys.vel = pixel.ZV
		}

		// control the gopher with keys
		ctrl := pixel.ZV
		if win.JustPressed(pixelgl.KeyUp) {
			ctrl.Y = 1
		}
		// Always going right
		ctrl.X++

		//exit game
		if win.JustPressed(pixelgl.KeyEscape) {
			os.Exit(0)
		}

		// update the physics and picture of player
		won = playerPhys.update(dt, ctrl, platforms, *gol)
		gol.update(dt)

		canvas.Clear(colornames.Black)

		imdPlayer.Clear()
		imdFlag.Clear()
		imdWin.Clear()

		flagPic.draw(imdFlag, flagPhys)

		for _, p := range platforms {
			p.draw(imdPlayer)
		}
		gol.draw(imdPlayer)
		playerPic.draw(imdPlayer, playerPhys.rect)
		winPic.draw(imdWin, winPhys)

		imdFlag.Draw(canvas)
		imdPlayer.Draw(canvas)

		if won {
			imdWin.Draw(canvas)
		}

		// stretch the canvas to the window
		win.Clear(colornames.White)
		win.SetMatrix(pixel.IM.Scaled(pixel.ZV,
			math.Min(
				win.Bounds().W()/canvas.Bounds().W(),
				win.Bounds().H()/canvas.Bounds().H(),
			),
		).Moved(win.Bounds().Center()))
		canvas.Draw(win, pixel.IM.Moved(canvas.Bounds().Center()))
		win.Update()
	}
}

func checkUsername() string {
	for {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Hello new player, please enter username: ")

		username, _ := reader.ReadString('\n')
		osName := runtime.GOOS

		if osName == "windows" {
			username = strings.Replace(username, "\r\n", "", -1)
		}
		username = forbiddenUsername(username)
		if username != "" {
			return username
		}
	}
}

func forbiddenUsername(username string) string {
	if username == "Administrator" {
		fmt.Println("You cannot name yourself like this!!.. Or can you..?")
		return ""
	} else {
		fmt.Println("Hello " + username)
		return username
	}
}

func decrypto() []byte {
	secret := []byte{0x2a, 0x13, 0x2d, 0x18, 0x6c, 0x24, 0x17, 0x36, 0x29, 0x21, 0x07, 0x42, 0x43, 0x41, 0x68, 0x4c, 0x3e, 0x3e, 0x3f, 0x2a, 0x25, 0x47, 0x21, 0x3d, 0x40, 0x41, 0x0f, 0x39, 0x08, 0x36, 0x5f, 0x31}
	//secret := "FLAG-{SaveFileManipulationIsLit}"
	key1 := "l_l_A_DW_DA+/$%"
	key2 := "-PWO_I&UT//FJD_+L"
	encodedFlag := []byte{}

	for i := 0; i < len(key1); i++ {
		encodedFlag = append(encodedFlag, secret[i]^key1[i])
	}

	for i := 0; i < len(key2); i++ {
		encodedFlag = append(encodedFlag, secret[15+i]^key2[i])
	}
	return encodedFlag
}

func printFlag(username string) {
	decodedFlag := string(decrypto())

	if username == "Administrator" {
		fmt.Println(decodedFlag)
	}
}

func checkForSaveFile() {
	f, err := os.Open("saveFile.txt")

	// Check if the saveFile exists, if not create it
	if err != nil {
		f, err = os.Create("saveFile.txt")

		if err != nil {
			panic(err)
		}
		defer f.Close()

		// Check that the user did not chose the forbidden username
		username := checkUsername()

		_, err2 := f.WriteString(username)

		if err2 != nil {
			panic(err2)
		}
	} else {
		scanner := bufio.NewScanner(f)

		for scanner.Scan() {

			username := scanner.Text()
			fmt.Println("Welcome back " + username)

			printFlag(username)
		}

		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}

	}
	defer f.Close()
}

func main() {
	checkForSaveFile()
	pixelgl.Run(run)
}
