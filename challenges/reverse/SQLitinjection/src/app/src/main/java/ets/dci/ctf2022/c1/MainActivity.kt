package ets.dci.ctf2022.c1

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity


class MainActivity : AppCompatActivity() {

    private lateinit var dbHandler: DBHandler

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        dbHandler = DBHandler(this);

        val courseNameEdt: EditText = findViewById(R.id.idEdtCourseName)
        val btnAddCourse: Button = findViewById(R.id.idBtnAddCourse)
        val searchResult: TextView = findViewById(R.id.idSearchResult)

        btnAddCourse.setOnClickListener(object : View.OnClickListener {
            override fun onClick(v: View?) {

                // below line is to get data from all edit text fields.
                val courseName = courseNameEdt.text.toString()

                val display = dbHandler.search(courseName)
                searchResult.text = display
            }
        })
    }
}