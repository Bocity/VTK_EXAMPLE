import vtk

def main():
	colors = vtk.vtkNamedColors()
	bkg = map(lambda x:x / 255.0,[26,51,102,255])
	colors.SetColor("BkgColor",*bkg)

	cylinder = vtk.vtkCylinderSource()
	cylinder.SetResolution(5)

	cylinderMapper = vtk.vtkPolyDataMapper()
	cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

	cylinderActor = vtk.vtkActor()
	cylinderActor.SetMapper(cylinderMapper)
	cylinderActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
	cylinderActor.RotateX(30.0)
	cylinderActor.RotateY(-45.0)


	ren = vtk.vtkRenderer()
	renWin = vtk.vtkRenderWindow()
	renWin.AddRenderer(ren)
	iren = vtk.vtkRenderWindowInteractor()
	iren.SetRenderWindow(renWin)

	ren.AddActor(cylinderActor)
	ren.SetBackground(colors.GetColor3d("BkgColor"))
	renWin.SetSize(300,300)
	renWin.SetWindowName('Cylinder')

	iren.Initialize()

	ren.ResetCamera()
	ren.GetActiveCamera().Zoom(1.5)
	renWin.Render()

	iren.Start()

if __name__ == '__main__':
	main()
